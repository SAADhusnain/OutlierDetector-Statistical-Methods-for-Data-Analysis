import numpy as np
import pandas as pd
from scipy import stats

# Sample dataset
data_file = pd.read_excel("Your DATA.xlsx")
# Select columns of interest
data = data_file[['Parameters', 'Parameters', 'Parameters', 'Parameters','Parameters']] #you can also include your target parameter/variable

### Method 1: Using Interquartile Range (IQR)

def calculate_outlier_threshold_iqr(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - (1.5 * IQR) 
    upper_bound = Q3 + (1.5 * IQR)
    return lower_bound, upper_bound

### Method 2: Using Standard Deviation

def calculate_outlier_threshold_std(data, std_dev_multiplier=3):
    mean = np.mean(data)
    std_dev = np.std(data)
    lower_bound = mean - (std_dev_multiplier * std_dev)
    upper_bound = mean + (std_dev_multiplier * std_dev)
    return lower_bound, upper_bound

### Method 3: Using Z-Score

def calculate_outlier_threshold_zscore(data, z_score_threshold=3):
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = [(x - mean) / std_dev for x in data]
    lower_bound = -z_score_threshold
    upper_bound = z_score_threshold
    return lower_bound, upper_bound, z_scores

# Apply each method to each column
for column_name in data.columns:
    column_data = data[column_name]
    
    # Method 1: IQR
    lower_iqr, upper_iqr = calculate_outlier_threshold_iqr(column_data)
    print(f"**{column_name} - IQR Method Outlier Threshold:** Below {lower_iqr} or Above {upper_iqr}")
    
    # Method 2: Standard Deviation
    lower_std, upper_std = calculate_outlier_threshold_std(column_data)
    print(f"**{column_name} - Standard Deviation Method Outlier Threshold (3 STD):** Below {lower_std} or Above {upper_std}")
    
    # Method 3: Z-Score
    # lower_z, upper_z, z_scores = calculate_outlier_threshold_zscore(column_data)
    # print(f"**{column_name} - Z-Score Method Outlier Threshold (Z={3}):**")
    # print(f"  - Data Points' Z-Scores: {z_scores}")
    # print(f"  - Threshold: Below {lower_z} or Above {upper_z}\n")
