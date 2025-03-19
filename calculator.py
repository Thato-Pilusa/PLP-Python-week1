import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+ or - or * or /): ")

if operation == "+":
    results = num1 + num2
    print(f"{num1} + {num2} = {results}")
elif operation == "-":
    results = num1 - num2
    print(f"{num1} - {num2} = {results}")
elif operation == "*":
    results = num1 * num2
    print(f"{num1} * {num2} = {results}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else: print( "Error: Division by zero is not allowed")
else:
    print ("Invalid operation! Please enter + or - or * or /")


