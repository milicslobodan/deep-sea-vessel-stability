
"""
Deep-Sea Vessel Stability Analysis
Step 3: Vessel particulars and weight distribution

Illustrative educational model, not approved ship data.
"""

from dataclasses import dataclass


@dataclass
class WeightItem:
    name: str
    weight_t: float
    kg_m: float


# --------------------------------------------------
# 1. Principal vessel particulars
# --------------------------------------------------

VESSEL_NAME = "Illustrative Deep-Sea Cargo Vessel"

LENGTH_M = 150.0
BREADTH_M = 23.0
DEPTH_M = 13.5
DRAFT_M = 8.2

DEADWEIGHT_T = 15000.0


# --------------------------------------------------
# 2. Weight distribution for one loading condition
#
# kg_m = vertical position above the keel
# All weights are in metric tonnes.
# --------------------------------------------------

weights = [
    WeightItem("Lightship", 6000.0, 7.0),
    WeightItem("Cargo", 7500.0, 7.5),
    WeightItem("Fuel oil", 800.0, 3.0),
    WeightItem("Diesel oil", 150.0, 3.0),
    WeightItem("Fresh water", 200.0, 2.5),
    WeightItem("Ballast water", 1000.0, 2.0),
    WeightItem("Stores and provisions", 150.0, 8.0),
]


# --------------------------------------------------
# 3. Calculate displacement and vertical moments
# --------------------------------------------------

displacement_t = sum(item.weight_t for item in weights)

vertical_moment_tm = sum(
    item.weight_t * item.kg_m for item in weights
)

KG_m = vertical_moment_tm / displacement_t


# --------------------------------------------------
# 4. Print the results
# --------------------------------------------------

print("=" * 60)
print("DEEP-SEA VESSEL STABILITY ANALYSIS")
print("STEP 3: VESSEL PARTICULARS AND WEIGHT DISTRIBUTION")
print("=" * 60)

print(f"\nVessel: {VESSEL_NAME}")

print("\nPRINCIPAL PARTICULARS")
print("-" * 40)
print(f"Length:              {LENGTH_M:.2f} m")
print(f"Breadth:             {BREADTH_M:.2f} m")
print(f"Depth:               {DEPTH_M:.2f} m")
print(f"Assumed draft:       {DRAFT_M:.2f} m")
print(f"Design deadweight:   {DEADWEIGHT_T:.0f} t")

print("\nWEIGHT DISTRIBUTION")
print("-" * 60)
print(f"{'Item':<25}{'Weight (t)':>14}{'KG (m)':>12}")

for item in weights:
    print(
        f"{item.name:<25}"
        f"{item.weight_t:>14,.1f}"
        f"{item.kg_m:>12.2f}"
    )

print("-" * 60)
print(f"{'Displacement':<25}{displacement_t:>14,.1f}")
print(f"{'Vertical moment (t*m)':<25}{vertical_moment_tm:>14,.1f}")

print(f"\nCalculated KG: {KG_m:.3f} m above keel")

print("\nENGINEERING NOTE")
print("These values are illustrative assumptions.")
print("Displacement, draft and hydrostatics must be")
print("consistent before assessing vessel stability.")
print("=" * 60)