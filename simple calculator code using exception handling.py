def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")

        print("Result:", result)

    except ValueError as ve:
        print("Value Error:", ve)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Run the calculator
calculator()
