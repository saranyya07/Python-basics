num1=float(input("Enter a first number: "))
num2=float(input("Enter a second number: "))
operator=input("Enter a operator(+,-,*,/,%,//,**): ")
match operator:
    case "+":
        result=num1+num2
    case "-":
        result=num1-num2
    case "*":
        result=num1*num2
    case "/":
        if num2 !=0:
            result=num1 /num2
        else:
            result="Error"
    case "%":
        if num2 !=0:
            result=num1%num2
        else:
            result="Error"
    case "//":
        if num2 !=0:
            result=num1//num2
        else:
            result="Error"
    case "**":
        result=num1**num2
    case _:
        result="invalid operator"
print("Result: ",result)