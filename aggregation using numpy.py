import numpy as np

# Get user input for array elements
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(float, user_input.split()))

# Convert list to numpy array
data = np.array(numbers)

# Aggregation operations
print(f"Original Data: {data}")
print(f"Sum: {np.sum(data)}")
print(f"Mean: {np.mean(data)}")
print(f"Maximum: {np.max(data)}")
print(f"Minimum: {np.min(data)}")
print(f"Standard Deviation: {np.std(data)}")
