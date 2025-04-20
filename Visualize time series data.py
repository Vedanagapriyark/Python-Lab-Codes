import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the time-series data (example: temperature over days)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Temperature': [22, 21, 23, 20, 19]
}

# Step 2: Convert to DataFrame and parse dates
df = pd.DataFrame(data)
print(“Temperature over days Data”)
print(df)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Step 3: Display basic statistics
print("Summary Statistics:\n", df.describe())

# Step 4: Plotting
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['Temperature'], marker='o', linestyle='-', color='teal')
plt.title("Daily Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
