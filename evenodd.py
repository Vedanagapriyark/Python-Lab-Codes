def separate_even_odd(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return evens, odds

# Input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Processing
evens, odds = separate_even_odd(numbers)

# Output
print("Even Numbers:", evens)
print("Odd Numbers:", odds)

OUTPUT:
Enter numbers separated by space: 8 9 7 6 0 5
Even Numbers: [8, 6, 0]
Odd Numbers: [9, 7, 5]
