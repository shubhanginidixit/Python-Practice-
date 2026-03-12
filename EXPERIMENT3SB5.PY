# Division with exception handling

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")

except ValueError:
    print("Error: Please enter valid integers.")

print("Program continues execution.")