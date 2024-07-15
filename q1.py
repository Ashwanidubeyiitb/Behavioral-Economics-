import pandas as pd
import numpy as np
from scipy.stats import skew, sem

# Load the dataset
file_path = r'C:\Users\Ashwani\Downloads\HIRAL\Stata.xlsx'
df = pd.read_excel(file_path)

# Select rows 1 to 63 and columns Q1 and Q2
sample_data = df.loc[161:183, ['Q1', 'Q2']]

# Number of bootstrap iterations
n_bootstraps = 1000

# Lists to store bootstrap results
bootstrapped_skewness_Q1 = []
bootstrapped_skewness_Q2 = []

# Perform bootstrap sampling and calculate skewness for Q1 and Q2
for _ in range(n_bootstraps):
    bootstrap_sample = sample_data.sample(frac=1, replace=True)
    bootstrapped_skewness_Q1.append(skew(bootstrap_sample['Q1']))
    bootstrapped_skewness_Q2.append(skew(bootstrap_sample['Q2']))

# Calculate bootstrap statistics
mean_skewness_Q1 = np.mean(bootstrapped_skewness_Q1)
mean_skewness_Q2 = np.mean(bootstrapped_skewness_Q2)
std_err_skewness_Q1 = sem(bootstrapped_skewness_Q1)
std_err_skewness_Q2 = sem(bootstrapped_skewness_Q2)

# Print the results
print('for DR')
print("Skewness (Q1): Mean =", mean_skewness_Q1, "Standard Error =", std_err_skewness_Q1)
print("Skewness (Q2): Mean =", mean_skewness_Q2, "Standard Error =", std_err_skewness_Q2)
