# Write a Python function that divides two numbers and handles the case where the divisor is zero by returning a custom error message.



def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
