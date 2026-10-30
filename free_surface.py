
"""
Deep-Sea Vessel Stability Analysis
Step 6: Illustrative free-surface correction

Rectangular tank approximations.
Not approved ship data.
"""

# Vessel loading condition
DISPLACEMENT_T = 15800.0
GM_UNCORRECTED_M = 4.620

# Illustrative partially filled tanks.
# Length and breadth are internal liquid dimensions.
# Density is in tonnes per cubic metre.
#
# These dimensions and liquid levels are assumptions,
# not verified particulars for the vessel.

tanks = [
    {
        "name": "Fuel oil tank",
        "length_m": 10.0,
        "breadth_m": 8.0,
        "density_t_m3": 0.90,
    },
    {
        "name": "Diesel oil tank",
        "length_m": 6.0,
        "breadth_m": 4.0,
        "density_t_m3": 0.85,
    },
    {
        "name": "Ballast water tank",
        "length_m": 12.0,
        "breadth_m": 7.0,
        "density_t_m3": 1.025,
    },
]


def calculate_free_surface_moment(tank):
    """
    Approximate FSM for a rectangular tank.

    FSM = liquid density * length * breadth**3 / 12
    Units: tonne-metres.
    """
    return (
        tank["density_t_m3"]
        * tank["length_m"]
        * tank["breadth_m"] ** 3
        / 12.0
    )


# Calculate each tank's free-surface moment
total_fsm_tm = 0.0

print("=" * 65)
print("STEP 6: FREE-SURFACE CORRECTION")
print("=" * 65)

print(
    f"{'Tank':<22}"
    f"{'FSM (t*m)':>15}"
)

print("-" * 40)

for tank in tanks:
    fsm_tm = calculate_free_surface_moment(tank)
    total_fsm_tm += fsm_tm

    print(
        f"{tank['name']:<22}"
        f"{fsm_tm:>15,.2f}"
    )

# Correction in metres
fsc_m = total_fsm_tm / DISPLACEMENT_T

# Illustrative corrected GM
gm_corrected_m = GM_UNCORRECTED_M - fsc_m

print("-" * 40)
print(f"Total FSM:              {total_fsm_tm:,.2f} t*m")
print(f"Displacement:           {DISPLACEMENT_T:,.1f} t")
print(f"Free-surface correction: {fsc_m:.4f} m")
print(f"Uncorrected GM:         {GM_UNCORRECTED_M:.3f} m")
print(f"Corrected GM estimate:  {gm_corrected_m:.3f} m")

print("\nIMPORTANT LIMITATIONS")
print("Tank dimensions and liquid densities are illustrative.")
print("Rectangular tank geometry is assumed.")
print("Actual tank free surfaces and approved hydrostatics")
print("must be used for a real vessel assessment.")
print("=" * 65)
