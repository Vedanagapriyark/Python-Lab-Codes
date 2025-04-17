import pandas as pd
import numpy as np

# Create a DataFrame with some missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, np.nan],
    'Score': [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Detect missing values
print("\nMissing Data (True = Missing):")
print(df.isnull())

# Fill missing values
df_filled = df.fillna({
    'Age': df['Age'].mean(),
    'Score': df['Score'].mean()
})
print("\nAfter Filling Missing Values:")
print(df_filled)

# Drop rows with any missing data
df_dropped = df.dropna()
print("\nAfter Dropping Rows with Missing Data:")
print(df_dropped)

OUTPUT:
Original Data:
      Name   Age  Score
0    Alice  25.0   85.0
1      Bob   NaN   90.0
2  Charlie  30.0    NaN
3    David   NaN   88.0

Missing Data (True = Missing):
    Name    Age  Score
0  False  False  False
1  False   True  False
2  False  False   True
3  False   True  False

After Filling Missing Values:
      Name   Age      Score
0    Alice  25.0  85.000000
1      Bob  27.5  90.000000
2  Charlie  30.0  87.666667
3    David  27.5  88.000000

After Dropping Rows with Missing Data:
    Name   Age  Score
0  Alice  25.0   85.0

