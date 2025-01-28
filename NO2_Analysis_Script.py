
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the NVH3 data from the CSV file
nvh3_path = 'path_to_your_NVH3_130pm_Data.csv'
nvh3_df = pd.read_csv(nvh3_path)

# Clean and prepare the NVH3 data
nvh3_df['PKT'] = pd.to_datetime(nvh3_df['PKT'])
nvh3_df['time'] = pd.to_datetime(nvh3_df['time'])
nvh3_df.rename(columns={'time': 'Measurement Date', 
                        ' mean_OMNO2d_003_ColumnAmountNO2TropCloudScreened': 'OMNO2d_NO2'}, inplace=True)

# Remove rows with negative values
nvh3_cleaned = nvh3_df[(nvh3_df['NO2 Tro'] >= 0) & (nvh3_df['OMNO2d_NO2'] >= 0)]

# Align the data based on the 'Measurement Date'
nvh3_aligned = nvh3_cleaned.drop(columns=['PKT']).drop_duplicates().sort_values(by='Measurement Date')

# Time Series Plot with Dual Y-Axes for Aligned Data
fig, ax1 = plt.subplots(figsize=(12, 6))
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('NO2 Tro Values', color=color)
ax1.plot(nvh3_aligned['Measurement Date'], nvh3_aligned['NO2 Tro'], color=color, label='NO2 Tro', marker='o', linestyle='-')
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('OMNO2d_NO2 Values', color=color)
ax2.plot(nvh3_aligned['Measurement Date'], nvh3_aligned['OMNO2d_NO2'], color=color, label='OMNO2d_NO2', marker='x', linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Time Series of Aligned NO2 Tro and OMNO2d_NO2 Values')
fig.tight_layout()
plt.show()

# Scatter Plot for Aligned Data
plt.figure(figsize=(10, 6))
plt.scatter(nvh3_aligned['NO2 Tro'], nvh3_aligned['OMNO2d_NO2'], color='darkcyan')
plt.title('Scatter Plot of Aligned NO2 Tro vs. OMNO2d_NO2 Values')
plt.xlabel('NO2 Tro Values')
plt.ylabel('OMNO2d_NO2 Values')
plt.grid(True)
plt.tight_layout()
plt.show()

# Save the aligned NVH3 data to a CSV file
output_csv_path = 'nvh3_aligned_data.csv'
nvh3_aligned.to_csv(output_csv_path, index=False)
