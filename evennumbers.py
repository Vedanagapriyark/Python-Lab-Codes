def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Output
print("Even Numbers:", filter_even_numbers(numbers))

OUTPUT:
Enter numbers separated by space: 2 34 0 9 8
Even Numbers: [2, 34, 0, 8]
