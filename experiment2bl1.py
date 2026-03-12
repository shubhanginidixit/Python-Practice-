import time

# Reusable decorator
def log_and_time(func):
    def wrapper(*args, **kwargs):
        print(f"Function called: {func.__name__}")
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        
        return result
    return wrapper


# Example function
@log_and_time
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


# Function call
print("Result:", calculate_sum(1000000))