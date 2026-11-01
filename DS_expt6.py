import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("cdsp-rainfall.csv")
# print(df.head())


data = df[['average_rainfall', 'highest_rainfall']]
data = data.dropna()
data.head()


# for column in data.columns:
#     values = data[column].values
#     mean = np.sum(values) / len(values)
#     print(column)
#     print("Mean =", mean)

# for column in data.columns:
#     values = data[column].values
#     values.sort()
#     n = len(values)
#     if n % 2 == 0:
#         median = (values[n//2] + values[(n//2)-1]) / 2
#     else:
#         median = values[n//2]
#     print(column)
#     print("Median =", median)

# for column in data.columns:
#     values = data[column].values
#     mean = np.sum(values) / len(values)
#     variance = np.sum((values - mean)**2) / len(values)
#     std = np.sqrt(variance)
#     print(column)
#     print("Standard Deviation =", std)


# plt.figure(figsize=(12, 5))
# plt.subplot(1, 2, 1)
# plt.hist(data['average_rainfall'], bins=50, color='skyblue', edgecolor='black', log=True)
# plt.xlabel("Average Rainfall (mm)")
# plt.ylabel("Frequency (Log Scale)")
# plt.title("Histogram of Average Rainfall")
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# plt.subplot(1, 2, 2)
# plt.hist(data['highest_rainfall'], bins=50, color='salmon', edgecolor='black', log=True)
# plt.xlabel("Highest Rainfall (mm)")
# plt.ylabel("Frequency (Log Scale)")
# plt.title("Histogram of Highest Rainfall")
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(10, 5))
# for column in data.columns:
#     values = data[column].values
#     values.sort()
#     probability = np.linspace(0, 1, len(values))
#     plt.plot(values, probability, label=column)

# plt.xlabel("Rainfall Values")
# plt.ylabel("Probability")
# plt.title("Density Plot of Rainfall Attributes")
# plt.legend()
# plt.show()


# for column in data.columns:
#     values = data[column].values
#     mean = np.sum(values) / len(values)
#     std = np.sqrt(
#         np.sum((values - mean)**2) / len(values)
#     )
#     skewness = (
#         np.sum((values - mean)**3) / len(values)
#     ) / (std**3)
#     print(column)
#     print("Skewness =", skewness)


# for column in data.columns:
#     values = data[column].values
#     values.sort()
#     Q1 = values[int(0.25 * len(values))]
#     Q3 = values[int(0.75 * len(values))]
#     IQR = Q3 - Q1
#     lower = Q1 - (1.5 * IQR)
#     upper = Q3 + (1.5 * IQR)
#     outliers = []
#     for x in values:
#         if x < lower or x > upper:
#             outliers.append(x)
#     print(column)
#     print("Q1 =", Q1)
#     print("Q3 =", Q3)
#     print("IQR =", IQR)
#     print("Lower Limit =", lower)
#     print("Upper Limit =", upper)
#     print("Number of Outliers =", len(outliers))


# values = data['average_rainfall'].values
# mean = np.mean(values)
# std = np.std(values)
# x = np.linspace(min(values), max(values), 500)
# normal_curve = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std)**2)
# plt.figure(figsize=(9, 5))
# plt.hist(values, bins=50, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Actual Data')
# plt.plot(x, normal_curve, color='red', linewidth=2.5, label='Normal Distribution')
# plt.xlim(-50, 1500)
# plt.xlabel("Average Rainfall (mm)")
# plt.ylabel("Probability Density")
# plt.title("Average Rainfall Compared with Normal Distribution")
# plt.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.show()


print("=== Summary Statistics ===")
print(data.describe())
print("\n=== Skewness ===")
print(data.skew())
print("\n=== Median ===")
print(data.median())






