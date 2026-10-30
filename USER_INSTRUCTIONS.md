# User Instructions
## Deep-Sea Vessel Stability Analysis

### 1. Purpose of the Project

This project demonstrates introductory ship stability calculations using Python.

It covers vessel particulars, approximate hydrostatics, free-surface correction, large-angle stability, numerical integration of the GZ curve, and comparison of hypothetical loading conditions.

The project is intended for educational purposes and Python engineering practice only.

**Safety notice:** The vessel data and KN table are illustrative. The results must not be used to determine the safe loading, stability, seaworthiness, or regulatory compliance of an actual vessel.

---

### 2. Project Location

The project folder is:

`C:\dev1\deep-sea-vessel-stability`

The project uses Python, NumPy, and Matplotlib.

---

### 3. Starting the Project

#### Step 1 — Open PowerShell

Open Windows PowerShell.

#### Step 2 — Navigate to the project folder

Enter:

```powershell
cd C:\dev1\deep-sea-vessel-stability
```

#### Step 3 — Activate the virtual environment

Enter:

```powershell
.\.venv\Scripts\Activate.ps1
```

The PowerShell prompt should begin with:

```text
(.venv) PS C:\dev1\deep-sea-vessel-stability>
```

The `(.venv)` prefix indicates that the project's virtual environment is active.

If the virtual environment is already active in the current PowerShell window, you do not need to activate it again.

#### Step 4 — Check the required packages

Enter:

```powershell
python -m pip show numpy matplotlib
```

If a package is missing, install both required packages with:

```powershell
python -m pip install numpy matplotlib
```

---

### 4. Running the Programs

Run each command from the project directory with the virtual environment activated.

#### Step 3 — Vessel Particulars

```powershell
python vessel_particulars.py
```

Calculates the assumed vessel displacement, vertical moments, and KG.

#### Step 4 — Hydrostatics

```powershell
python hydrostatics.py
```

Estimates underwater volume and block coefficient.

#### Step 5 — Approximate Hydrostatics

```powershell
python hydrostatics_approx.py
```

Estimates KB, BM, KM, and initial GM using simplified assumptions.

#### Step 6 — Free-Surface Correction

```powershell
python free_surface.py
```

Demonstrates how assumed partially filled tanks affect corrected GM.

#### Step 7 — Large-Angle Stability

```powershell
python large_angle_stability.py
```

Calculates and plots an illustrative GZ curve using the fabricated KN table.

#### Step 8 — GZ Curve Area and Stability Checks

```powershell
python stability_checks.py
```

Calculates areas under the GZ curve, checks the initial slope, and runs automated numerical checks.

#### Step 9 — Loading Condition Comparison

```powershell
python loading_condition_comparison.py
```

Compares hypothetical loading conditions with higher, baseline, and lower KG values.

**Note:** The filenames above must match the files present in the project directory. If a command reports that a file cannot be found, check the filename using `Get-ChildItem -File`.

---

### 5. Viewing the Generated Graphs

The programs generate image files in the project directory.

#### Step 7 graph

`gz_curve_illustrative.png`

#### Step 8 graph

`gz_curve_step8_area.png`

#### Step 9 graph

`loading_condition_comparison.png`

To open the Step 8 graph from PowerShell:

```powershell
Start-Process .\gz_curve_step8_area.png
```

To open the Step 9 graph:

```powershell
Start-Process .\loading_condition_comparison.png
```

To check whether a graph exists:

```powershell
Get-ChildItem -Filter "*.png"
```

The graphs are created when the corresponding Python programs run successfully.

---

### 6. Understanding the Main Results

#### Displacement

Displacement is the assumed total mass of the vessel and its contents, expressed in tonnes.

#### KG

KG is the vertical distance from the keel to the vessel's centre of gravity.

#### GM

GM is the metacentric height. In this project, corrected GM is estimated by subtracting KG and the free-surface correction from the approximate KM.

#### GZ

GZ is the righting arm, which represents the lever associated with the restoring moment at a given heel angle.

#### Righting moment

The project calculates the mass-based righting moment in tonne-metres:

Righting moment = displacement × GZ

Multiplying the result by gravitational acceleration converts tonne-metres into a physical torque in N·m.

#### Area under the GZ curve

The area is calculated numerically over the heel-angle range. The integration uses radians, so the result is expressed in m·rad.

#### Loading condition comparison

The comparison illustrates how changing KG affects the calculated GM and GZ curve when the other model inputs are held constant.

---

### 7. Understanding Automated Checks

The Step 8 and Step 9 programs perform basic checks on their calculated results.

A `PASS` indicates that the specified numerical condition was satisfied.

A `FAIL` indicates that the condition was not satisfied. For example, a zero crossing may not be detected within the calculated angle range.

A failed check should be investigated and explained. It should not simply be removed or changed to obtain a passing result.

Passing all checks confirms only that the tested relationships are consistent with the selected model and assumptions. It does not validate the vessel's actual stability.

---

### 8. Common Problems

#### Problem: NumPy is missing

Error:

```text
ModuleNotFoundError: No module named 'numpy'
```

Solution:

```powershell
python -m pip install numpy matplotlib
```

Make sure the virtual environment is active before installing the packages.

#### Problem: The Python file cannot be found

Check the current directory:

```powershell
Get-Location
```

It should be:

`C:\dev1\deep-sea-vessel-stability`

List the Python files:

```powershell
Get-ChildItem -Filter "*.py"
```

#### Problem: The graph does not appear

Check whether the image was saved:

```powershell
Get-ChildItem -Filter "*.png"
```

If the file exists, open it with `Start-Process`, using its actual filename.

#### Problem: The virtual environment is not activated

Run:

```powershell
cd C:\dev1\deep-sea-vessel-stability
.\.venv\Scripts\Activate.ps1
```

---

### 9. Important Engineering Limitations

This project uses simplified hydrostatic estimates, assumed loading data, hypothetical tank properties, and a fabricated KN table.

The model does not represent a validated hull or complete ship stability assessment. It does not comprehensively evaluate downflooding, trim, changing displacement, or applicable regulatory criteria.

The project must not be used for real-world vessel operations, cargo planning, safe draft decisions, stability approval, or certification.

Real vessel assessments require validated vessel data and suitable professional engineering review.

---

### 10. Recommended Workflow

For each study session:

1. Open PowerShell.
2. Navigate to the project directory.
3. Activate the virtual environment.
4. Run the desired Python program.
5. Read the printed results.
6. Review the graph, if generated.
7. Investigate errors or failed checks.
8. Keep a record of important results and changes.

To leave the virtual environment when finished, enter:

```powershell
deactivate
```

You can close PowerShell after finishing your work. The next time you return, open a new PowerShell window and repeat the startup instructions.

---

**Project:** Deep-Sea Vessel Stability Analysis  
**Document:** User Instructions  
**Purpose:** Educational use and Python engineering practice  
**Status:** Educational demonstration only
