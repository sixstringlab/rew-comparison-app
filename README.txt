# SPL Comparison Project

## Overview

The SPL Comparison project is a tool for analyzing and comparing the sound pressure level (SPL) measurements of different audio equipment. By taking one baseline SPL measurement (e.g., a real amplifier) and comparing it against other measurements (e.g., modelers or plugins), users can assess how similar the responses are. The results are expressed as a percentage similarity to the baseline.

### Included Comparison Files
The project includes the following SPL measurement files:
- `badcat.txt`: Baseline measurement from a real amplifier (Bad Cat).
- `headrush.txt`: Measurement from a Headrush modeler.
- `nam.txt`: Measurement from Neural Amp Modeler (NAM).
- `tonex.txt`: Measurement from IK Multimedia Tonex.

## Features
- Parses SPL data files in text format.
- Filters data to focus on the range of **80 Hz to 8000 Hz**.
- Interpolates comparison data to match the baseline frequency resolution.
- Calculates a percentage similarity between the baseline and comparison files.

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- `pip` (Python package manager)

### Step 1: Clone the Repository
```bash
# Clone the GitHub repository
git clone https://github.com/sixstringlab/spl-comparison.git

# Navigate into the project directory
cd spl-comparison
```

### Step 2: Create a Virtual Environment
Set up an isolated Python environment for the project:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required Python libraries:
```bash
pip install numpy pandas
```

---

## Running the Project

### Usage
To run the script, use the following command:
```bash
python spl_comparison.py <baseline_file> <comparison_file1> [comparison_file2 ...]
```

### Example
To compare the included files:
```bash
python spl_comparison.py badcat.txt headrush.txt nam.txt tonex.txt
```

### Expected Output
The script will output similarity percentages for each comparison file relative to the baseline. For example:
```
Reading baseline file: badcat.txt
Filtered data (80Hz - 8000Hz) from badcat.txt:
...

Reading comparison file: headrush.txt
...
headrush.txt: 85.32% similarity to baseline
nam.txt: 88.45% similarity to baseline
tonex.txt: 92.17% similarity to baseline
```

---

## File Format Requirements

The SPL data files must follow this format:
- Lines starting with `*` are comments or metadata.
- The header line defining columns must read:
  ```
  * Freq(Hz), SPL(dB), Phase(degrees)
  ```
- Data rows contain numeric values for frequency, SPL, and phase.

### Example File (badcat.txt)
```
* Measurement data measured by REW V5.31.3
* Source: Pro Tools Audio Bridge 16
* Format: 512k Log Swept Sine, 1 sweep at -12.0 dBFS
* Dated: Dec 10, 2024 11:18:04 PM
* Freq(Hz), SPL(dB), Phase(degrees)
20.141602, 63.013, 29.3247
20.507813, 62.773, 33.4853
...
```

---

## Contributing

We welcome contributions! To contribute:
1. Fork the repository on GitHub.
2. Create a feature branch.
3. Submit a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## About
This project is developed by **Six String Lab** to provide audio professionals with a reliable way to compare SPL measurements across different audio gear. For more information, visit [Six String Lab](https://sixstringlab.com).
