# Deep-Sea Vessel Stability Analysis

## 1. Project Overview

This project is an educational Python application demonstrating basic naval architecture and ship stability calculations.

It explores vessel particulars, approximate hydrostatics, free-surface corrections, large-angle stability, numerical integration of the righting-arm curve, and the influence of different vertical centres of gravity.

The project uses Python, NumPy, and Matplotlib to perform calculations, display numerical results, generate graphs, and compare hypothetical loading conditions.

**Important:** This project is intended for education and programming practice only. It is not an approved ship stability calculation, stability booklet, or assessment of the safety or seaworthiness of an actual vessel.

## 2. Project Objectives

The main objectives are to:

- Calculate displacement and the vertical centre of gravity (KG) from assumed weight data.
- Estimate underwater volume and the block coefficient.
- Introduce the concepts of KB, BM, KM, and metacentric height (GM).
- Apply an illustrative free-surface correction.
- Calculate and plot an illustrative righting-arm (GZ) curve.
- Estimate the area under the GZ curve using numerical integration.
- Compare hypothetical loading conditions with different KG values.
- Practise Python programming, numerical analysis, plotting, and automated checks.

## 3. Software Requirements

- Python 3.11 or later recommended
- NumPy
- Matplotlib
- Windows, Linux, or macOS

The project was developed and tested in a Windows PowerShell environment using a Python virtual environment.

## 4. Installation

### Step 1 — Open the project directory

In PowerShell:

```powershell
cd C:\dev1\deep-sea-vessel-stability
```

### Step 2 — Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3 — Install dependencies

```powershell
python -m pip install numpy matplotlib
```

### Step 4 — Run a program

For example, to run the Step 8 stability checks:

```powershell
python stability_checks.py
```

To compare the illustrative loading conditions:

```powershell
python loading_condition_comparison.py
```

## 5. Project Development Steps

### Step 3 — Vessel Particulars

**File:** `vessel_particulars.py`

Introduces the vessel's principal dimensions, assumed loading weights, and vertical centres of gravity.

Illustrative input data:

- Length: 150 m
- Breadth: 23 m
- Depth: 13.5 m
- Assumed draft: 8.2 m
- Total displacement: 15,800 t

Calculated results:

- Total vertical moment: 104,800 t·m
- Vertical centre of gravity, KG: approximately 6.633 m

The loading data are hypothetical and do not represent a verified vessel loading condition.

### Step 4 — Hydrostatics

**File:** `hydrostatics.py`

Calculates an estimated underwater volume using seawater density and the assumed displacement.

Illustrative results:

- Seawater density: 1.025 t/m³
- Underwater volume: approximately 15,414.63 m³
- Estimated block coefficient: approximately 0.5449

The block coefficient is based on the assumed principal dimensions and estimated underwater volume.

### Step 5 — Approximate Hydrostatics

**File:** `hydrostatics_approx.py`

Introduces approximate calculations of:

- KB — vertical position of the centre of buoyancy
- BM — metacentric radius
- KM — height of the metacentre above the keel
- GM — metacentric height

Illustrative results:

- KB: 4.346 m
- BM: 6.907 m
- KM: 11.253 m
- Uncorrected GM: 4.620 m

These values are approximate and are not derived from actual hull lines or validated hydrostatic tables.

### Step 6 — Free-Surface Correction

**File:** `free_surface.py`

Demonstrates how partially filled tanks can reduce effective initial stability.

Illustrative results:

- Total assumed free-surface moment: 762.77 t·m
- Free-surface correction: approximately 0.0483 m
- Corrected GM: approximately 4.572 m

Tank dimensions and liquid properties are assumed for educational purposes.

### Step 7 — Large-Angle Stability

**File:** `large_angle_stability.py`

Introduces the KN cross-curve concept and calculates an illustrative righting arm:

GZ = KN − KG × sin(heel angle)

The effective KG includes the assumed free-surface correction.

Illustrative results:

- Maximum GZ: approximately 2.255 m
- Heel angle at maximum GZ: 40°
- Calculated zero crossing: approximately 66°

The KN values are fabricated demonstration data, not values obtained from the actual vessel's hull geometry.

### Step 8 — GZ Curve Area and Stability Checks

**File:** `stability_checks.py`

Calculates the area under the illustrative GZ curve using numerical integration with the trapezoidal method.

Illustrative results:

- Area from 0° to 30°: approximately 0.5867 m·rad
- Area from 0° to 40°: approximately 0.9681 m·rad
- Area from 0° to 60°: approximately 1.5992 m·rad
- Area to the illustrative zero crossing: approximately 1.6512 m·rad

The program also checks the initial GZ slope, corrected GM, maximum GZ, and the existence of a zero crossing within the calculated range.

The eight checks passed for the selected illustrative data. These checks demonstrate numerical consistency; they do not validate the underlying vessel model.

Generated graph:

`gz_curve_step8_area.png`

### Step 9 — Loading Condition Comparison

**File:** `loading_condition_comparison.py`

Compares three hypothetical conditions while holding displacement, free-surface correction, and illustrative KN data constant:

- Higher KG: baseline KG + 1.0 m
- Baseline: calculated KG
- Lower KG: baseline KG − 1.0 m

Illustrative comparison:

| Condition | KG (m) | Corrected GM (m) | Maximum GZ (m) |
|---|---:|---:|---:|
| Higher KG | 7.633 | 3.572 | 1.644 |
| Baseline | 6.633 | 4.572 | 2.255 |
| Lower KG | 5.633 | 5.572 | 2.898 |

The higher-KG and lower-KG cases demonstrate the expected direction of change in the calculated stability parameters.

For the lower-KG case, a zero crossing was not detected within the 0°–70° calculation range. This does not prove that a zero crossing does not exist at a larger angle.

Generated graph:

`loading_condition_comparison.png`

## 6. Main Engineering Concepts

The project introduces the following relationships.

### Displacement and underwater volume

For displacement expressed in tonnes:

Volume = Displacement / seawater density

### Vertical centre of gravity

KG = total vertical moment / total displacement

### Initial metacentric height

GM = KM − KG

When a free-surface correction is included:

Corrected GM = KM − KG − free-surface correction

### Righting arm

For the illustrative KN method:

GZ = KN − KG_effective × sin(heel angle)

### Righting moment

Righting moment = displacement × GZ

When displacement is expressed in tonnes and GZ in metres, the result is in tonne-metres. Conversion to physical torque in N·m requires multiplication by gravitational acceleration.

### Area under the GZ curve

The area under GZ plotted against heel angle is evaluated with numerical integration. Heel angles must be expressed in radians for the resulting area to have units of m·rad.

These equations are simplified educational relationships. Their use in a real vessel assessment requires appropriate validated input data and the applicable naval architecture methods.

## 7. Generated Graphs

The project generates the following images when the corresponding programs are run:

- `gz_curve_illustrative.png`
- `gz_curve_step8_area.png`
- `loading_condition_comparison.png`

The images illustrate the calculated curves and comparisons. They should always be interpreted alongside the assumptions and limitations described in this document.

## 8. Limitations and Safety Notice

This project has significant limitations:

1. The vessel's dimensions and loading data are assumed.
2. The hydrostatic calculations use simplified approximations.
3. The free-surface moments are based on hypothetical tank dimensions and liquid properties.
4. The KN table is fabricated and is not derived from the actual hull geometry.
5. The calculations do not account comprehensively for downflooding, openings, trim, changing displacement, or all relevant stability criteria.
6. Automated checks assess numerical relationships within the selected model, not real-world vessel safety.
7. The project has not been validated against an approved stability booklet or professional naval architecture analysis.

**Do not use the outputs to make operational decisions, determine safe loading limits, approve a vessel for service, or establish regulatory compliance.**

A real ship stability assessment requires reliable vessel hydrostatics, a verified loading condition, appropriate free-surface data, downflooding information, and assessment by suitably qualified professionals against applicable requirements.

## 9. Possible Future Improvements

Possible extensions for a future version include:

- Importing verified hydrostatic and KN tables.
- Using actual vessel loading conditions and tank data.
- Adding trim and displacement-dependent hydrostatic calculations.
- Reading input data from CSV files.
- Producing a consolidated calculation report.
- Adding unit tests and regression tests.
- Comparing results against trusted reference calculations.
- Implementing applicable intact-stability criteria using validated data.

These extensions should only be considered after suitable source data and validation methods are available.

## 10. Conclusion

The `deep-sea-vessel-stability` project demonstrates how Python can support introductory naval architecture calculations and engineering data visualization.

It provides practical experience with physical equations, numerical integration, plotted results, automated checks, and sensitivity studies involving hypothetical loading conditions.

The project is an educational model, not a validated representation of an actual ship.

---

**Project:** Deep-Sea Vessel Stability Analysis  
**Purpose:** Education and Python engineering practice  
**Status:** Educational demonstration project  
