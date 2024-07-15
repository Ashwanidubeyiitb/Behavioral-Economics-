import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, sem

# Load the dataset
file_path = r'C:\Users\Ashwani\Downloads\HIRAL\Stata.xlsx'
df = pd.read_excel(file_path)

# Number of bootstrap iterations
n_bootstraps = 1000

# Define function for bootstrap analysis, skewness calculation, and histogram plotting
def process_feature(feature, start_row, end_row, color):
    # Select rows for the current feature
    sample_data = df.loc[start_row:end_row, [feature]]

    # Lists to store bootstrap results
    bootstrapped_skewness = []

    # Perform bootstrap sampling and calculate skewness for the current feature
    for _ in range(n_bootstraps):
        bootstrap_sample = sample_data.sample(frac=1, replace=True)
        bootstrapped_skewness.append(skew(bootstrap_sample[feature]))

    # Calculate bootstrap statistics
    mean_skewness = np.mean(bootstrapped_skewness)
    std_err_skewness = sem(bootstrapped_skewness)

    # Print the results
    print(f"Skewness ({feature}): Mean =", mean_skewness, "Standard Error =", std_err_skewness)

    # Plot histogram for the current feature
    plt.figure(figsize=(8, 6))
    plt.hist(sample_data[feature], bins=20, color=color, alpha=0.75)
    plt.title(f'Histogram of {feature}')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    # plt.show()

# Process each feature separately
process_feature('NI', 0, 55, 'blue')  # NI from row 1 to 63
process_feature('II', 56, 100, 'green')  # II from row 64 to 116
process_feature('DI', 101, 144, 'orange')  # DI from row 117 to 161
process_feature('DR', 161, 183, 'red')  # DR from row 162 to 205
