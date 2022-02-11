def operate():
    operator=input("enter the sign")
    num1=int(input("enter the no"))
    num2=int(input("enter the no"))
    if operator=='+':
        print( num1 + num2)
    elif operator=='-':
        print(num1 - num2)
    elif operator=='*':
        print(num1 * num2)
    else:
        return num1 / num2
operate()