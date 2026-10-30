
"""
Deep-Sea Vessel Stability Analysis
Step 8: GZ curve area and numerical stability checks

EDUCATIONAL DEMONSTRATION ONLY.

The KN data are fabricated illustrative values.
This program is not suitable for real vessel safety decisions.
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Vessel loading condition (from previous steps)
# --------------------------------------------------

DISPLACEMENT_T = 15800.0
KG_M = 104800.0 / DISPLACEMENT_T
FSC_M = 762.77 / DISPLACEMENT_T
KG_EFFECTIVE_M = KG_M + FSC_M

KM_APPROX_M = 11.253
GM_CORRECTED_M = KM_APPROX_M - KG_EFFECTIVE_M

# --------------------------------------------------
# 2. Illustrative KN table from Step 7
# --------------------------------------------------

heel_table_deg = np.array([
    0, 5, 10, 15, 20, 25, 30, 35,
    40, 45, 50, 55, 60, 65, 70
], dtype=float)

KN_table_m = np.array([
    0.00, 0.98, 1.95, 2.90, 3.80,
    4.65, 5.40, 6.05, 6.55, 6.90,
    7.05, 7.00, 6.75, 6.25, 5.55
], dtype=float)

# --------------------------------------------------
# 3. Calculate GZ at 1-degree intervals
# --------------------------------------------------

heel_deg = np.arange(0.0, 70.1, 1.0)
heel_rad = np.radians(heel_deg)

KN_m = np.interp(
    heel_deg, heel_table_deg, KN_table_m
)

GZ_m = KN_m - KG_EFFECTIVE_M * np.sin(heel_rad)

# --------------------------------------------------
# 4. Find maximum GZ and zero crossing
# --------------------------------------------------

max_index = int(np.argmax(GZ_m))
max_GZ_m = GZ_m[max_index]
max_GZ_angle_deg = heel_deg[max_index]

zero_crossing_deg = None

for i in range(1, len(GZ_m)):
    if GZ_m[i - 1] > 0 and GZ_m[i] <= 0:
        fraction = GZ_m[i - 1] / (
            GZ_m[i - 1] - GZ_m[i]
        )
        zero_crossing_deg = (
            heel_deg[i - 1]
            + fraction * (heel_deg[i] - heel_deg[i - 1])
        )
        break

# --------------------------------------------------
# 5. Calculate areas under the GZ curve
#    Integration uses radians, so area units are m·rad.
# --------------------------------------------------

def area_to_angle(limit_deg):
    """Integrate GZ from upright to a specified angle."""
    mask = heel_deg <= limit_deg

    x_rad = heel_rad[mask]
    y_gz = GZ_m[mask]

    # Include the exact requested endpoint if needed.
    if limit_deg > heel_deg[mask][-1]:
        endpoint_gz = np.interp(
            limit_deg, heel_deg, GZ_m
        )
        x_rad = np.append(x_rad, np.radians(limit_deg))
        y_gz = np.append(y_gz, endpoint_gz)

    return float(np.trapezoid(y_gz, x_rad))


area_0_30 = area_to_angle(30.0)
area_0_40 = area_to_angle(40.0)
area_0_60 = area_to_angle(60.0)

area_to_zero = None

if zero_crossing_deg is not None:
    mask = heel_deg < zero_crossing_deg

    area_angles_rad = np.append(
        heel_rad[mask],
        np.radians(zero_crossing_deg)
    )

    area_gz = np.append(
        GZ_m[mask],
        0.0
    )

    area_to_zero = float(
        np.trapezoid(area_gz, area_angles_rad)
    )

# --------------------------------------------------
# 6. Check initial slope against corrected GM
# --------------------------------------------------

# The initial slope of GZ with respect to heel angle
# in radians should approximately equal corrected GM.
small_angle_rad = np.radians(5.0)

initial_slope_m = (
    GZ_m[5] - GZ_m[0]
) / small_angle_rad

# --------------------------------------------------
# 7. Automated numerical checks
# --------------------------------------------------

checks = {
    "GZ is approximately zero at upright":
        abs(GZ_m[0]) < 1e-9,

    "Corrected GM is positive":
        GM_CORRECTED_M > 0,

    "Maximum GZ is positive":
        max_GZ_m > 0,

    "Maximum GZ occurs within the calculated range":
        0 <= max_GZ_angle_deg <= 70,

    "Zero crossing is within the calculated range":
        zero_crossing_deg is not None
        and 0 < zero_crossing_deg <= 70,

    "Area to 30 degrees is positive":
        area_0_30 > 0,

    "Area to 60 degrees is positive":
        area_0_60 > 0,

    "Initial slope is reasonably close to corrected GM":
        abs(initial_slope_m - GM_CORRECTED_M) < 0.5,
}

# --------------------------------------------------
# 8. Print results
# --------------------------------------------------

print("=" * 65)
print("STEP 8: GZ CURVE AREA AND STABILITY CHECKS")
print("=" * 65)

print("\nLOADING CONDITION")
print("-" * 65)
print(f"Displacement:               {DISPLACEMENT_T:.1f} t")
print(f"KG:                         {KG_M:.3f} m")
print(f"Free-surface correction:    {FSC_M:.4f} m")
print(f"Effective KG:               {KG_EFFECTIVE_M:.3f} m")
print(f"Approx. corrected GM:       {GM_CORRECTED_M:.3f} m")

print("\nGZ CURVE RESULTS")
print("-" * 65)
print(f"Maximum GZ:                 {max_GZ_m:.3f} m")
print(f"Angle of maximum GZ:        {max_GZ_angle_deg:.1f} degrees")
print(f"Initial slope at 5 degrees: {initial_slope_m:.3f} m/rad")
print(f"Corrected GM for comparison:{GM_CORRECTED_M:8.3f} m")

print("\nAREA UNDER THE GZ CURVE")
print("-" * 65)
print(f"Area from 0 to 30 degrees:  {area_0_30:.4f} m·rad")
print(f"Area from 0 to 40 degrees:  {area_0_40:.4f} m·rad")
print(f"Area from 0 to 60 degrees:  {area_0_60:.4f} m·rad")

if area_to_zero is not None:
    print(f"Area to zero crossing:      {area_to_zero:.4f} m·rad")
    print(f"Positive-stability range:   0 to {zero_crossing_deg:.1f} degrees")
else:
    print("Positive-stability endpoint: not found")

print("\nAUTOMATED CHECKS")
print("-" * 65)

for description, passed in checks.items():
    status = "PASS" if passed else "FAIL"
    print(f"{status:6}  {description}")

print("-" * 65)
print(f"Checks passed: {sum(checks.values())}/{len(checks)}")

print("\nIMPORTANT LIMITATION")
print("The KN data are fabricated illustrative values.")
print("Passing these checks does not establish vessel safety.")
print("Actual stability requires validated hull hydrostatics,")
print("loading data, free-surface data, downflooding points,")
print("and assessment against applicable stability criteria.")

# --------------------------------------------------
# 9. Plot GZ curve and area up to zero crossing
# --------------------------------------------------

plt.figure(figsize=(10, 6))
plt.plot(heel_deg, GZ_m, label="Illustrative GZ curve")

if zero_crossing_deg is not None:
    positive_mask = heel_deg <= zero_crossing_deg

    plt.fill_between(
        heel_deg[positive_mask],
        GZ_m[positive_mask],
        0,
        where=GZ_m[positive_mask] >= 0,
        alpha=0.25,
        label="Positive GZ area"
    )

    plt.axvline(
        zero_crossing_deg,
        linestyle=":",
        label=f"Zero crossing: {zero_crossing_deg:.1f}°"
    )

plt.axhline(0.0, linewidth=1)

plt.scatter(
    [max_GZ_angle_deg],
    [max_GZ_m],
    label="Maximum GZ"
)

plt.xlabel("Heel angle (degrees)")
plt.ylabel("Righting arm GZ (m)")
plt.title("Step 8: Illustrative GZ Curve and Positive Area")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("gz_curve_step8_area.png", dpi=150)
plt.show()

print("\nGraph saved as: gz_curve_step8_area.png")
