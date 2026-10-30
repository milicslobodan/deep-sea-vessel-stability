
"""
Deep-Sea Vessel Stability Analysis
Step 7: Large-angle GZ curve

EDUCATIONAL DEMONSTRATION ONLY.

The KN table below is illustrative placeholder data.
It is NOT derived from the actual hull geometry.
Do not use this curve for ship operation or certification.
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Loading condition and centre of gravity
# --------------------------------------------------

DISPLACEMENT_T = 15800.0
KG_M = 104800.0 / 15800.0
FSC_M = 762.77 / DISPLACEMENT_T

KG_EFFECTIVE_M = KG_M + FSC_M

# Approximate KM from Step 5, for comparison only
KM_APPROX_M = 11.253

GM_CORRECTED_M = KM_APPROX_M - KG_EFFECTIVE_M

# --------------------------------------------------
# 2. Illustrative KN cross-curve table
#
# These values are fabricated for demonstrating
# the calculation. They are not verified hull data.
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
# 3. Calculate righting arms
# --------------------------------------------------

heel_deg = np.arange(0.0, 70.1, 1.0)
heel_rad = np.radians(heel_deg)

# Interpolate the illustrative KN values
KN_m = np.interp(
    heel_deg,
    heel_table_deg,
    KN_table_m
)

# Corrected righting arm
GZ_m = KN_m - KG_EFFECTIVE_M * np.sin(heel_rad)

# Righting moment in tonne-metres
righting_moment_tm = DISPLACEMENT_T * GZ_m

# --------------------------------------------------
# 4. Identify numerical results
# --------------------------------------------------

max_index = int(np.argmax(GZ_m))
max_GZ_m = GZ_m[max_index]
max_GZ_angle_deg = heel_deg[max_index]

# Find first positive-to-nonpositive crossing
zero_crossing_deg = None

for i in range(1, len(GZ_m)):
    if GZ_m[i - 1] > 0 and GZ_m[i] <= 0:
        # Linear interpolation between adjacent points
        fraction = GZ_m[i - 1] / (
            GZ_m[i - 1] - GZ_m[i]
        )
        zero_crossing_deg = (
            heel_deg[i - 1]
            + fraction * (heel_deg[i] - heel_deg[i - 1])
        )
        break

# --------------------------------------------------
# 5. Print results
# --------------------------------------------------

print("=" * 65)
print("STEP 7: LARGE-ANGLE STABILITY DEMONSTRATION")
print("=" * 65)

print(f"Displacement:              {DISPLACEMENT_T:.1f} t")
print(f"KG:                        {KG_M:.3f} m")
print(f"Free-surface correction:   {FSC_M:.4f} m")
print(f"Effective KG:              {KG_EFFECTIVE_M:.3f} m")
print(f"Approx. corrected GM:      {GM_CORRECTED_M:.3f} m")

print("\nILLUSTRATIVE GZ RESULTS")
print("-" * 65)
print(f"Maximum GZ:                {max_GZ_m:.3f} m")
print(f"Heel at maximum GZ:        {max_GZ_angle_deg:.1f} degrees")
print(f"Righting moment at max GZ: "
      f"{DISPLACEMENT_T * max_GZ_m:,.0f} t*m")

if zero_crossing_deg is not None:
    print(f"Illustrative GZ zero crossing: "
          f"{zero_crossing_deg:.1f} degrees")
else:
    print("No positive-to-nonpositive crossing found.")

print("\nWARNING")
print("The KN table is fabricated educational data.")
print("The resulting maximum GZ and zero crossing are")
print("NOT valid estimates for an actual vessel.")
print("Downflooding and regulatory criteria are not assessed.")

print("\nGZ TABLE")
print("-" * 40)
print(f"{'Heel (deg)':>10} {'KN (m)':>10} {'GZ (m)':>10}")

for angle in range(0, 71, 5):
    i = int(angle)
    print(
        f"{heel_deg[i]:10.1f}"
        f"{KN_m[i]:10.3f}"
        f"{GZ_m[i]:10.3f}"
    )

# --------------------------------------------------
# 6. Plot GZ curve
# --------------------------------------------------

plt.figure(figsize=(10, 6))
plt.plot(heel_deg, GZ_m, label="Illustrative corrected GZ")
plt.axhline(0.0, linewidth=1)
plt.axvline(max_GZ_angle_deg, linestyle="--",
            label="Angle of maximum GZ")

plt.xlabel("Heel angle (degrees)")
plt.ylabel("Righting arm GZ (m)")
plt.title("Illustrative Large-Angle Stability Curve")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("gz_curve_illustrative.png", dpi=150)
plt.show()
