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

OUTPUT:
Enter numbers separated by spaces: 2 4 8 9
Original Data: [2. 4. 8. 9.]
Sum: 23.0
Mean: 5.75
Maximum: 9.0
Minimum: 2.0
Standard Deviation: 2.8613807855648994
