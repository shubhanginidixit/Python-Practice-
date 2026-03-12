import time

# Decorator to measure execution time
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"Function: {func.__name__} | Execution Time: {end - start:.6f} seconds")
        
        return result
    return wrapper


# Example functions
@time_decorator
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


@time_decorator
def multiply(a, b):
    return a * b


# Function calls
calculate_sum(1000000)
multiply(10, 20)