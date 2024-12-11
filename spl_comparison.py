import sys
import numpy as np
import pandas as pd

def read_spl_file(file_path):
    """Read an SPL data file and return a DataFrame."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the line where data starts
    header_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith("* Freq(Hz), SPL(dB), Phase(degrees)"):
            header_line = i
            break

    if header_line is None:
        raise ValueError(f"No header line found in file: {file_path}")

    # Read the data into a DataFrame
    data = pd.read_csv(
        file_path,
        skiprows=header_line + 1,
        names=["Freq(Hz)", "SPL(dB)", "Phase(degrees)"]
    )
    print(f"Data read from {file_path}:")
    print(data.head())

    # Filter data between 80Hz and 6000Hz
    data = data[(data["Freq(Hz)"] >= 80) & (data["Freq(Hz)"] <= 8000)]
    print(f"Filtered data (80Hz - 8000Hz) from {file_path}:")
    print(data.head())
    return data

def calculate_similarity(baseline, comparison):
    """Calculate the percentage similarity between the baseline and comparison SPL data."""
    # Interpolate comparison to match the baseline frequencies
    comparison_interp = np.interp(baseline["Freq(Hz)"], comparison["Freq(Hz)"], comparison["SPL(dB)"])

    # Log interpolated values
    print(f"Interpolated comparison data (first 10 values): {comparison_interp[:10]}")

    # Calculate the absolute deviation
    deviation = np.abs(baseline["SPL(dB)"] - comparison_interp)

    # Log deviation values
    print(f"Deviation values (first 10 values): {deviation[:10]}")

    # Normalize to get similarity percentage
    similarity = 100 - (np.sum(deviation) / np.sum(np.abs(baseline["SPL(dB)"])) * 100)
    return similarity

def main():
    if len(sys.argv) < 3:
        print("Usage: python compare_spl.py baseline_file comparison_file1 [comparison_file2 ...]")
        sys.exit(1)

    # Read baseline file
    baseline_file = sys.argv[1]
    print(f"Reading baseline file: {baseline_file}")
    try:
        baseline_data = read_spl_file(baseline_file)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Iterate through comparison files
    results = []
    for comparison_file in sys.argv[2:]:
        print(f"Reading comparison file: {comparison_file}")
        try:
            comparison_data = read_spl_file(comparison_file)
            similarity = calculate_similarity(baseline_data, comparison_data)
            results.append(f"{comparison_file}: {similarity:.2f}% similarity to baseline")
        except ValueError as e:
            print(f"Error reading {comparison_file}: {e}")

    # Print results
    if not results:
        print("No results were generated.")
    else:
        print("\nComparison Results:")
        print("\n".join(results))

if __name__ == "__main__":
    main()
