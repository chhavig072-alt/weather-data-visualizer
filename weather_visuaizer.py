import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STEP 0: Create Dummy Data (For Testing Only)
# ==========================================
def create_dummy_data():
    dates = pd.date_range(start='2023-01-01', periods=100)
    np.random.seed(42)
    data = {
        'Date': dates,
        'Temperature': np.random.uniform(10, 35, size=100),
        'Rainfall': np.random.choice([0, 0, 0, 5, 10, 20], size=100),
        'Humidity': np.random.uniform(30, 90, size=100)
    }
    df = pd.DataFrame(data)

    # Introduce missing values
    df.loc[5:10, 'Temperature'] = np.nan
    df.loc[15:20, 'Humidity'] = np.nan

    df.to_csv('weather_dataset.csv', index=False)
    print("✓ Dummy dataset 'weather_dataset.csv' created.")

create_dummy_data()

# ==========================================
# TASK 1: Data Acquisition and Loading
# ==========================================
print("\n--- TASK 1: LOADING DATA ---")
filename = 'weather_dataset.csv'
df = pd.read_csv(filename)

print("Data Loaded Successfully.")
print(df.head())

# ==========================================
# TASK 2: Data Cleaning and Processing
# ==========================================
print("\n--- TASK 2: CLEANING DATA ---")

df['Date'] = pd.to_datetime(df['Date'])

# Fill missing values
temp_mean = df['Temperature'].mean()
df['Temperature'] = df['Temperature'].fillna(temp_mean)
df['Humidity'] = df['Humidity'].ffill()
df['Rainfall'] = df['Rainfall'].fillna(0)

# Keep required columns
df = df[['Date', 'Temperature', 'Rainfall', 'Humidity']]

print("Data Cleaned. Missing values remaining:", df.isnull().sum().sum())

# ==========================================
# TASK 3: Statistical Analysis with NumPy
# ==========================================
print("\n--- TASK 3: STATISTICS (NumPy) ---")

temps = df['Temperature'].to_numpy()
rain = df['Rainfall'].to_numpy()

print(f"Temperature - Mean: {np.mean(temps):.2f}, Max: {np.max(temps):.2f}, Min: {np.min(temps):.2f}")
print(f"Rainfall - Total: {np.sum(rain):.2f}, Max Daily: {np.max(rain):.2f}")
print(f"Standard Deviation (Temp): {np.std(temps):.2f}")

# ==========================================
# TASK 4: Visualization with Matplotlib
# ==========================================
print("\n--- TASK 4: VISUALIZ
