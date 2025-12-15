# 🔷 GeoFrame - Norman Window Optimizer

**Interactive application for calculating and visualizing optimal dimensions of Norman windows**

---

## 📑 Table of Contents

- [📖 Project Description](#-project-description)
- [🎯 Mathematical Problem](#-mathematical-problem)
- [📐 Mathematical Foundation](#-mathematical-foundation)
- [⚡ Features](#-features)
- [🔧 Technical Implementation](#-technical-implementation)
- [💾 Installation](#-installation)
- [🖥️ Display Configuration](#️-display-configuration)
- [🚀 Usage](#-usage)
- [📂 Project Structure](#-project-structure)
- [🎓 Academic Context](#-academic-context)
- [📜 License](#-license)
- [👤 Author](#-author)

---

## 📖 Project Description

**GeoFrame** is a scientific application developed in Python that solves a classic **constrained optimization problem**: finding the optimal dimensions of a Norman window that **maximize its area** given a **fixed perimeter**.

This project was conceived as an educational tool to visualize and understand advanced mathematical concepts such as optimization, derivatives, and practical applications of calculus in architectural design.

### 🏛️ What is a Norman Window?

A **Norman window** (also known as a semicircular window or Romanesque window) is an architectural structure composed of:
- A **rectangle** with base `x` and height `y`
- A **semicircle** with radius `r = x/2` placed on top of the rectangle's base

This classic architectural design combines structural stability with aesthetics, and presents an interesting mathematical challenge: **How do you distribute a limited perimeter to obtain the maximum possible area?**

---

## 🎯 Mathematical Problem

### 💡 The Challenge

Imagine you have a window frame with a fixed perimeter `P` (for example, 12 meters of material). How should you design the window so that the **maximum amount of light** (area) enters?

This is not an intuitive problem because:
- If you make the window too wide, the height decreases
- If you make it too tall, the width and semicircle become smaller
- The optimal balance requires calculus and optimization techniques

### 🔢 System Variables

```
x = Rectangle width (and semicircle diameter)
y = Rectangle height
r = Semicircle radius = x/2
P = Total perimeter (constraint)
A = Total area (function to maximize)
```

---

## 📐 Mathematical Foundation

### 1️⃣ Constraint Equation (Perimeter)

The perimeter of a Norman window consists of:
- Rectangle base: `x`
- Two vertical sides: `2y`
- Semicircumference on top: `πr = π(x/2)`

**Perimeter constraint:**
```
P = x + 2y + πx/2
P = x(1 + π/2) + 2y
```

Solving for `y`:
```
y = (P - x(1 + π/2)) / 2
```

### 2️⃣ Objective Function (Area)

The total area is the sum of:
- Rectangle area: `A_rect = xy`
- Semicircle area: `A_semi = πr²/2 = π(x/2)²/2 = πx²/8`

**Total area function:**
```
A(x) = xy + πx²/8
```

Substituting `y` from the constraint:
```
A(x) = x · [(P - x(1 + π/2))/2] + πx²/8
A(x) = (Px)/2 - x²(1 + π/2)/2 + πx²/8
A(x) = (Px)/2 - x²/2 - πx²/4 + πx²/8
A(x) = (Px)/2 - x²/2 - πx²/8
```

### 3️⃣ Optimization (Finding the Maximum)

To find the maximum, we take the derivative and set it equal to zero:

```
dA/dx = P/2 - x - πx/4 = 0
P/2 = x(1 + π/4)
x_optimal = P / (2 + π/2)
```

Once we have `x_optimal`, we calculate:
```
y_optimal = (P - x_optimal(1 + π/2)) / 2
A_max = x_optimal · y_optimal + π(x_optimal)²/8
```

### 4️⃣ Verification (Second Derivative Test)

To confirm it's a maximum (not a minimum):
```
d²A/dx² = -1 - π/4 < 0  ✓ (This confirms it's a maximum)
```

---

## ⚡ Features

### 🎮 Core Functionality
- **Automatic optimization:** Calculates optimal dimensions (x, y, r) using advanced numerical methods (SciPy)
- **Real-time updates:** All visualizations update dynamically as the perimeter changes
- **Interactive slider:** Adjust perimeter from 1 to 100 meters with 0.1 precision
- **Quick presets:** Buttons for common values (5, 12, 25, 50, 100 meters)

### 📊 Visualization Panels

**1. 🖼️ Norman Window Panel**
- Interactive geometric representation
- Annotated dimensions with arrows
- Three visualization modes:
  - **Normal:** Clean, basic view
  - **Detailed:** Grid lines and multiple layers
  - **Technical:** Complete specifications with partial areas

**2. 📈 Area vs Width Graph**
- Plot of area function A(x)
- Visual identification of the maximum point
- Reference lines to optimal dimensions
- Dynamic annotation with coordinates

**3. 📋 Numerical Results Panel**
- Input data display
- Optimal dimensions (x, y, r)
- Partial areas (rectangle and semicircle)
- All values with 4 decimal precision

**4. 🔍 Sensitivity Analysis Graph**
- Shows how maximum area varies with perimeter
- Range from 1 to 100 meters
- Current point highlighting
- Useful for "what-if" analysis

### ⚙️ Performance Optimizations

- **Smart caching:** Stores previously calculated results to avoid redundant computations
- **Precalculation:** Sensitivity data is computed once and reused
- **Efficient updates:** Only recalculates when perimeter changes significantly
- **History management:** Maintains a record of the last 20 calculations

---

## 🔧 Technical Implementation

### 🛠️ Technologies Used

**Core Libraries:**
- **Python 3.8+:** Main programming language
- **Matplotlib 3.5+:** Advanced plotting and visualization
- **PyQt5:** Graphical user interface and window management
- **NumPy:** Numerical computations and array operations
- **SciPy:** Advanced optimization algorithms (`minimize_scalar`)
- **Seaborn:** Professional styling for graphics

### 🧮 Optimization Algorithm

The application uses **SciPy's `minimize_scalar`** with the **bounded method**:

```python
from scipy.optimize import minimize_scalar

def negative_area(x):
    # Returns negative area for minimization
    y = (P - x*(1 + π/2)) / 2
    return -(x*y + π*x²/8)

result = minimize_scalar(
    negative_area,
    bounds=(0.01, P/(1 + π/2)),
    method='bounded'
)

x_optimal = result.x
max_area = -result.fun
```

This method guarantees finding the global maximum within the valid range.

### 🏗️ Architecture

The application follows **Object-Oriented Programming** principles:
- **Class `GeoFrame`:** Main application controller
- **Separation of concerns:** Each panel has its own update method
- **Event-driven design:** Responds to user interactions (slider, buttons, radio buttons)
- **Modular structure:** Easy to maintain and extend

---

## 💾 Installation

### ✅ Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
```

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/TheNarratorVIMXXX/GeoFrame.git
cd GeoFrame
```

### 📦 Step 2: Install Dependencies

```bash
pip install matplotlib PyQt5 numpy scipy seaborn
```

Or use the requirements file (if provided):

```bash
pip install -r requirements.txt
```

### ▶️ Step 3: Run the Application

```bash
python geoframe.py
```

---

## 🖥️ Display Configuration

### 📺 Recommended Settings for Optimal Visualization

For the best visual experience with **GeoFrame**, we recommend the following display settings:

#### **Display Resolution**
- **Recommended:** 1920 × 1080 (Full HD)
- This resolution ensures all panels, graphs, and controls are displayed properly without overlapping

#### **Scale and Layout (Windows)**
The application's interface is optimized for two specific zoom levels:

**Option 1: 150% Scale (Recommended)**
- Best balance between visibility and screen space
- Ideal for high-DPI displays
- All text and controls are comfortably readable
- Graphs maintain optimal proportions

**Option 2: 100% Scale**
- Maximum screen real estate
- All panels visible simultaneously
- Best for larger monitors (24" or above)
- Recommended for detailed analysis sessions

#### **How to Adjust Display Settings (Windows 10/11)**

1. Right-click on your desktop and select **Display settings**
2. Under **Scale and layout**, find the **Display resolution** dropdown
   - Set to **1920 × 1080 (Recommended)**
3. In the same section, find the **Scale** dropdown
   - Choose either **100%** or **150%** based on your preference
4. Click **Apply** and restart the GeoFrame application

#### ⚠️ Important Notes

- **Other resolutions:** The application will work on other resolutions, but layout may not be optimal
- **Other scales:** Using scales like 125% or 175% may cause minor alignment issues
- **Multiple monitors:** If using multiple displays, ensure GeoFrame runs on the monitor with the recommended settings

---

## 🚀 Usage

### 🎯 Basic Operation

1. **Launch the application:** Run the main Python file
2. **Adjust the perimeter:** Use the interactive slider or preset buttons
3. **Observe results:** All panels update automatically
4. **Change visualization mode:** Use radio buttons (Normal/Detailed/Technical)
5. **Analyze sensitivity:** Check how area changes with different perimeters

### 📊 Interpretation of Results

**Example with P = 12 meters:**
```
Optimal Width (x):     4.2667 m
Optimal Height (y):    1.6234 m
Semicircle Radius (r): 2.1333 m
Maximum Area:          13.5752 m²
```

This means that with 12 meters of perimeter, the design that lets in the most light is a window 4.27 meters wide and 1.62 meters tall, with a total area of 13.58 square meters.

---

## 📂 Project Structure

```
GeoFrame/
│
├── geoframe.py           # Main application file
├── LICENSE.md            # EVSL license
├── README.md             # This file
├── requirements.txt      # Python dependencies
│
└── imgs/
    └── logo.ico          # Application icon
```

---

## 🎓 Academic Context

This project was developed as part of the academic curriculum at:

- **Institution:** Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128 (CBTis 128)
- **Subject:** Mathematics III
- **Grade:** 3rd Year, Group "J"
- **Academic Period:** December 2025
- **Educational Objective:** Apply calculus concepts (derivatives, optimization, constrained functions) to solve real engineering and architecture problems

### 🎯 Skills Developed

- Advanced calculus and mathematical optimization
- Scientific programming in Python
- Data visualization and user interface design
- Algorithm optimization and performance
- Technical documentation

---

## 📜 License

This project is protected under the **Educational Visualization Software License (EVSL)**.

### ✅ Summary

**You MAY:**
- View and study the source code
- Learn from the implementation
- Run the software for educational purposes
- Cite the code in academic work

**You MAY NOT:**
- Redistribute the code (in whole or in part)
- Copy code fragments into other projects
- Modify and share altered versions
- Use commercially

### 📄 Full License

For complete terms and conditions, see the [LICENSE.md](LICENSE.md) file.

### 📝 Citation

If you use this project for academic reference, please cite as:

```
Magallanes López, C. G. (2025). GeoFrame - Norman Window Optimizer.
Centro de Bachillerato Tecnológico Industrial y de Servicios No. 128.
https://github.com/TheNarratorVIMXXX/GeoFrame
```

---

## 👤 Author

**Carlos Gabriel Magallanes López**

- **Institution:** CBTis No. 128
- **Email:** cgmagallanes23@gmail.com
- **GitHub:** [@TheNarratorVIMXXX](https://github.com/TheNarratorVIMXXX)
- **Date:** December 2025

---

## 🙏 Acknowledgments

Special thanks to:
- The Mathematics III teaching staff at CBTis 128
- The Python and open-source communities for excellent libraries
- All students and educators who use this tool for learning

---

**© 2025 Carlos Gabriel Magallanes López. All rights reserved.**

*This project represents the culmination of mathematical learning applied to software development, demonstrating that abstract concepts can solve real-world problems.*
