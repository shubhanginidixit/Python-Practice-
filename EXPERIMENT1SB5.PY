import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Decorator
def log_function(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function called: {func.__name__}")
        logging.info(f"Arguments: {args}, {kwargs}")

        result = func(*args, **kwargs)

        logging.info(f"Return value: {result}")
        return result
    return wrapper


# Example function
@log_function
def add(a, b):
    return a + b


# Function call
add(10, 5)