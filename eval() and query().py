import pandas as pd

# --------- eval() Example ---------
expression = input("Enter a mathematical expression (e.g., 2 + 3 * (4 - 1)): ")
result = eval(expression)
print("Result of eval():", result)

# --------- query() Example ---------
# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 95, 80]
}
df = pd.DataFrame(data)

# Show original data
print("\nDataFrame:")
print(df)

# Use query to filter data
condition = input("\nEnter a filter condition for query (e.g., Age > 28 and Score >= 90): ")
filtered_df = df.query(condition)

print("\nFiltered Data using query():")
print(filtered_df)

OUTPUT:
Enter a mathematical expression (e.g., 2 + 3 * (4 - 1)): 2 + 3 * (4 - 1)
Result of eval(): 11

DataFrame:
      Name  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     95
3    David   28     80

Enter a filter condition for query (e.g., Age > 28 and Score >= 90): Age>28

Filtered Data using query():
      Name  Age  Score
1      Bob   30     90
2  Charlie   35     95

