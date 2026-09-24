from logic import *

print("\n========== Simple Calculator =======")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:

    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Calculator Closed")
    
    choice = input("Enter your choice: ")

    match choice:

        case "1":
            print("Result =", addnum(num1,num2))

        case "2":
            print("Result =", multinum(num1,num2))        

        case "3":
            print("Calculator closed.")
            break

        case _:
            print("Invalid choice!")