
"""
Deep-Sea Vessel Stability Analysis
Step 5: Approximate initial hydrostatics

Educational estimate only.
Not suitable for operational safety decisions.
"""

# Vessel particulars
LENGTH_M = 150.0
BREADTH_M = 23.0
DRAFT_M = 8.2

DISPLACEMENT_T = 15800.0
SEAWATER_DENSITY_T_M3 = 1.025

# From Step 3
KG_M = 104800.0 / 15800.0

# Explicitly assumed approximation parameters
KB_RATIO = 0.53
WATERPLANE_COEFFICIENT = 0.70

# --------------------------------------------------
# 1. Displacement volume
# --------------------------------------------------

VOLUME_M3 = DISPLACEMENT_T / SEAWATER_DENSITY_T_M3

# --------------------------------------------------
# 2. Approximate centre of buoyancy
# --------------------------------------------------

KB_M = KB_RATIO * DRAFT_M

# --------------------------------------------------
# 3. Approximate waterplane second moment of area
#
# Rectangular waterplane approximation, adjusted by
# an assumed waterplane coefficient.
# --------------------------------------------------

I_WATERPLANE_M4 = (
    WATERPLANE_COEFFICIENT
    * LENGTH_M
    * BREADTH_M**3
    / 12.0
)

# --------------------------------------------------
# 4. Metacentric radius and height
# --------------------------------------------------

BM_M = I_WATERPLANE_M4 / VOLUME_M3

KM_M = KB_M + BM_M

GM_UNCORRECTED_M = KM_M - KG_M

# --------------------------------------------------
# 5. Report
# --------------------------------------------------

print("=" * 60)
print("STEP 5: APPROXIMATE INITIAL HYDROSTATICS")
print("=" * 60)

print(f"Displacement:              {DISPLACEMENT_T:.1f} t")
print(f"Underwater volume:         {VOLUME_M3:.2f} m3")
print(f"Draft:                     {DRAFT_M:.2f} m")
print(f"KG:                        {KG_M:.3f} m")

print("\nAPPROXIMATE HYDROSTATIC VALUES")
print("-" * 60)
print(f"KB:                        {KB_M:.3f} m")
print(f"Waterplane inertia:        {I_WATERPLANE_M4:.2f} m4")
print(f"BM:                        {BM_M:.3f} m")
print(f"KM:                        {KM_M:.3f} m")
print(f"Uncorrected GM:            {GM_UNCORRECTED_M:.3f} m")

print("\nLIMITATIONS")
print("KB ratio and waterplane coefficient are assumed.")
print("The hull geometry has not been verified.")
print("Free-surface correction has not been applied.")
print("This GM is an estimate, not an approved result.")

print("=" * 60)
