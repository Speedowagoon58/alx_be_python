# User input
first_number = float(input("Enter the first number:"))
second_number = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

# Result 
match operation:
    case "+":
        result = first_number + second_number
        print(f"The result is {result}.")
    case "-":
        result = first_number - second_number
        print(f"The result is {result}.")
    case "*":
        result = first_number * second_number
        print(f"The result is {result}.")
    case "/":
        if second_number != 0:
            result = first_number / second_number
            print(f"The result is {result}.")
        else: 
            print("Cannot devide by zero.")
    case _:
        print("Invalid operation selected.")