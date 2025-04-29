def calculator() :

    num1 = float(input("Enter the first number :"))
    operator = input("Select the operator : '+','-','*','/','%' :  ")
    num2 = float(input("Enter the second number :"))

    if operator == '+' :
        print("Result is : ", num1 + num2)
    elif operator == '-' :
        print("Result is : ", num1 - num2)
    elif operator == '*' :
        print("Result is : ", num1 * num2)
    elif operator == '/' :
        if num2 != 0 :
            print("Result is :", num1 / num2)
        else :
            print("Division by zero is not possible. Enter a valid number !!")
    elif operator == '%' :
        print("Result is :", num1 % num2)
    else :
        print("Enter a valid operation !!")

calculator()