# Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).



def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

# Example usage
print(arithmetic_operation(10, 5, '+'))
print(arithmetic_operation(10, 5, '/'))
print(arithmetic_operation(10, 0, '/'))
