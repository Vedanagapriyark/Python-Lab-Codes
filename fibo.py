def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Input
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci(n))
