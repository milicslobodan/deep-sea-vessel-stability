
"""
Deep-Sea Vessel Stability Analysis
Step 4: Displacement and hull consistency check

Illustrative educational model.
This is not a complete hydrostatic calculation.
"""

# Vessel particulars
LENGTH_M = 150.0
BREADTH_M = 23.0
DRAFT_M = 8.2

DISPLACEMENT_T = 15800.0

# Seawater density
SEAWATER_DENSITY_T_M3 = 1.025

# Calculate underwater volume
displacement_volume_m3 = (
    DISPLACEMENT_T / SEAWATER_DENSITY_T_M3
)

# Volume of a rectangular block with the same
# principal dimensions and draft
rectangular_volume_m3 = (
    LENGTH_M * BREADTH_M * DRAFT_M
)

# Implied block coefficient
block_coefficient = (
    displacement_volume_m3 / rectangular_volume_m3
)

print("=" * 55)
print("STEP 4: DISPLACEMENT AND HULL CHECK")
print("=" * 55)

print(f"Length:                  {LENGTH_M:.2f} m")
print(f"Breadth:                 {BREADTH_M:.2f} m")
print(f"Draft:                   {DRAFT_M:.2f} m")
print(f"Displacement:            {DISPLACEMENT_T:.1f} t")
print(f"Seawater density:        {SEAWATER_DENSITY_T_M3:.3f} t/m3")

print(f"\nUnderwater volume:       {displacement_volume_m3:.2f} m3")
print(f"Rectangular volume:      {rectangular_volume_m3:.2f} m3")
print(f"Implied block coefficient: {block_coefficient:.4f}")

print("\nINTERPRETATION")
print(
    "The block coefficient represents the ratio between "
    "underwater volume and L x B x draft."
)
print(
    "This value is implied by our assumptions; it is not "
    "verified hull data."
)
print(
    "Accurate KB, BM, KM and large-angle GZ require "
    "additional hull and hydrostatic information."
)

print("=" * 55)
