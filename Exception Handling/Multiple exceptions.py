try:
    num1 =int(input("Enter first number: "))
    num2 =int(input("Enter second number: "))
    result = num1 / num2
    print("The result is:", result)

except ValueError as ve:
    print("Invalid input! Please enter a valid integer.")
    print(ve)
except ZeroDivisionError as zde:
    print("Error! Second number cannot be zero.")
    print(zde)
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")