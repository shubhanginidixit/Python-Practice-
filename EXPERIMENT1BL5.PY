# Memoization decorator
def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return wrapper


# Recursive Fibonacci with memoization
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Dynamic input
n = int(input("Enter n: "))

for i in range(n):
    print(fibonacci(i))