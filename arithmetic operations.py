# Lambda functions for arithmetic operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Undefined"

# Input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
# Output
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))

