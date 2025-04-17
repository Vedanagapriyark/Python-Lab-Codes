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

OUTPUT:
Enter first number: 2
Enter second number: 3
Addition: 5.0
Subtraction: -1.0
Multiplication: 6.0
Division: 0.6666666666666666

