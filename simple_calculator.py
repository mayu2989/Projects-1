while True:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print("----------------Operation list----------------")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-----------------------------------------------")
    choice=int(input("Enter your choice: "))    
    match choice:
        case 1:
            print("Addition of two numbers is: ",num1+num2)
        case 2:
            print("Subtraction of two numbers is: ",num1-num2)
        case 3:
            print("Multiplication of two numbers is: ",num1*num2)
        case 4:
            print("Division of two numbers is: ",num1/num2)
        case 5:
            print("Exiting the calculator")
            print("Thank you for using the calculator")
            break
        case _:
            print("Invalid choice")
print("-----------------------------------------------")