def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That wasn't a valid number. Try again.")

def get_operation():
    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op in ops:
            return ops[op]
        print("Invalid operation. Please select one of +, -, *, /.") 

def welcome_message():
    print("""
    *************
    *                                   *
    *     Welcome to PyCalc 2024!       *
    *   Your personal CLI Calculator    *
    *                                   *
    *************
    """)

def goodbye_message():
    print("""
    *************
    *                                   *
    *  Thanks for using PyCalc 2024!    *
    *      Have a great day ahead!      *
    *                                   *
    *************
    """)

def main():
    welcome_message()
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()
        result = operation(num1, num2)
        print(f"The result is: {result}")  
        
        cont = input("Want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            break
    goodbye_message()

if __name__ == "__main__": 
    main()