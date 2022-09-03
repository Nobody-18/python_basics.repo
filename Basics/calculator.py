num1 = float(input("enter the first number"))
op = input("enter the operator")
num2 = float(input("enter the second number"))
if op == "+":
    ans = num1 + num2
    print(str(num1)+op + str(num2)+"="+str(ans))
elif op == "-":
    ans = num1 - num2
    print(str(num1)+op + str(num2)+"="+str(ans))
elif op == "*":
    ans = num1 * num2
    print(str(num1)+op + str(num2)+"="+str(ans))
elif op == "/":
    ans = num1 / num2
    print(str(num1)+op + str(num2)+"="+str(ans))
elif op == "%":
    ans = num1 % num2
    print(str(num1)+op + str(num2)+" = "+str(ans))
else:
    print("invalid operator")
