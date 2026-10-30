
"""
Deep-Sea Vessel Stability Analysis
Step 9: Comparison of illustrative loading conditions

EDUCATIONAL DEMONSTRATION ONLY.
The KN table is fabricated and is not based on real hull geometry.
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Common vessel data
# --------------------------------------------------

DISPLACEMENT_T = 15800.0
BASE_KG_M = 104800.0 / DISPLACEMENT_T
FSC_M = 762.77 / DISPLACEMENT_T
KM_APPROX_M = 11.253

# Illustrative KN data carried forward from Step 7
heel_table_deg = np.array([
    0, 5, 10, 15, 20, 25, 30, 35,
    40, 45, 50, 55, 60, 65, 70
], dtype=float)

KN_table_m = np.array([
    0.00, 0.98, 1.95, 2.90, 3.80,
    4.65, 5.40, 6.05, 6.55, 6.90,
    7.05, 7.00, 6.75, 6.25, 5.55
], dtype=float)

heel_deg = np.arange(0.0, 70.1, 1.0)
heel_rad = np.radians(heel_deg)
KN_m = np.interp(heel_deg, heel_table_deg, KN_table_m)

# --------------------------------------------------
# 2. Define three hypothetical loading conditions
# --------------------------------------------------
# KG changes are illustrative, not recalculated from
# actual cargo, tank, or ballast movements.

conditions = {
    "Higher KG (+1.0 m)": BASE_KG_M + 1.0,
    "Baseline": BASE_KG_M,
    "Lower KG (-1.0 m)": BASE_KG_M - 1.0,
}

results = {}

# --------------------------------------------------
# 3. Calculate each condition
# --------------------------------------------------

for name, kg_m in conditions.items():
    effective_kg_m = kg_m + FSC_M
    corrected_gm_m = KM_APPROX_M - effective_kg_m

    gz_m = KN_m - effective_kg_m * np.sin(heel_rad)

    max_index = int(np.argmax(gz_m))
    max_gz_m = float(gz_m[max_index])
    max_angle_deg = float(heel_deg[max_index])

    zero_crossing_deg = None

    for i in range(1, len(gz_m)):
        if gz_m[i - 1] > 0 and gz_m[i] <= 0:
            fraction = gz_m[i - 1] / (
                gz_m[i - 1] - gz_m[i]
            )
            zero_crossing_deg = float(
                heel_deg[i - 1]
                + fraction * (heel_deg[i] - heel_deg[i - 1])
            )
            break

    results[name] = {
        "kg": kg_m,
        "effective_kg": effective_kg_m,
        "gm": corrected_gm_m,
        "gz": gz_m,
        "max_gz": max_gz_m,
        "max_angle": max_angle_deg,
        "zero_crossing": zero_crossing_deg,
    }

# --------------------------------------------------
# 4. Print comparison table
# --------------------------------------------------

print("=" * 80)
print("STEP 9: LOADING CONDITION COMPARISON")
print("=" * 80)
print("Displacement and illustrative KN data are held constant.")
print("KG changes are hypothetical sensitivity tests.")

print(f"\nDisplacement: {DISPLACEMENT_T:.1f} t")
print(f"Free-surface correction: {FSC_M:.4f} m")

print("\nCOMPARISON RESULTS")
print("-" * 80)
print(
    f"{'Condition':<23}"
    f"{'KG (m)':>9}"
    f"{'GM (m)':>10}"
    f"{'Max GZ (m)':>13}"
    f"{'Angle (deg)':>13}"
    f"{'Zero (deg)':>12}"
)
print("-" * 80)

for name, r in results.items():
    zero_text = (
        f"{r['zero_crossing']:.1f}"
        if r["zero_crossing"] is not None
        else "not found"
    )

    print(
        f"{name:<23}"
        f"{r['kg']:>9.3f}"
        f"{r['gm']:>10.3f}"
        f"{r['max_gz']:>13.3f}"
        f"{r['max_angle']:>13.1f}"
        f"{zero_text:>12}"
    )

# --------------------------------------------------
# 5. Basic consistency checks
# --------------------------------------------------

higher = results["Higher KG (+1.0 m)"]
baseline = results["Baseline"]
lower = results["Lower KG (-1.0 m)"]

checks = {
    "Higher KG gives lower corrected GM":
        higher["gm"] < baseline["gm"],

    "Lower KG gives higher corrected GM":
        lower["gm"] > baseline["gm"],

    "All conditions have positive initial GM":
        all(r["gm"] > 0 for r in results.values()),

    "All conditions have a positive maximum GZ":
        all(r["max_gz"] > 0 for r in results.values()),

    "All conditions have a detected zero crossing":
        all(r["zero_crossing"] is not None for r in results.values()),
}

print("\nAUTOMATED CHECKS")
print("-" * 80)

for description, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL':6} {description}")

print("-" * 80)
print(f"Checks passed: {sum(checks.values())}/{len(checks)}")

# --------------------------------------------------
# 6. Plot the three illustrative GZ curves
# --------------------------------------------------

plt.figure(figsize=(10, 6))

for name, r in results.items():
    plt.plot(heel_deg, r["gz"], label=name)

plt.axhline(0.0, linewidth=1)
plt.xlabel("Heel angle (degrees)")
plt.ylabel("Righting arm GZ (m)")
plt.title("Step 9: Illustrative Loading Condition Comparison")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("loading_condition_comparison.png", dpi=150)
plt.show()

print("\nGraph saved as: loading_condition_comparison.png")
print("\nWARNING: This comparison is educational only.")
print("It does not establish actual vessel stability or compliance.")
