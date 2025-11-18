# Simple calculator:
print("\nChoose 2 numbers and what operation you want to execute with them:")
n=0
m=0
K=0
error=bool(False)
Num1=float(input("Choose the first number:"))
Operation=str(input("Choose the operation. You can choose between +, -, /, *. If you want to end the process press K on your keyboard:"))
Num2=float(input("Choose the second number:"))
if Operation != "+" and Operation != "-" and Operation != "/" and Operation != "*":
     n=1
     error=True
while n == 0:
    if Operation == "+":
        s = Num1 + Num2
    elif Operation == "-":
        s = Num1 - Num2
    elif Operation == "/":
        s = Num1 / Num2
    elif Operation == "*":
        s = Num1 * Num2
    print(f"The result is {s}")
    Operation = str(input("Choose the operation. You can choose between +, -, /, *. If you want to end the process press K on your keyboard."))
    if Operation == "k" or Operation == "K":
        m = 1
        K = 1
        break
    if Operation != "+" and Operation != "-" and Operation != "/" and Operation != "*":
        error=True
        m = 1
        break
    Num3 = float(input("Choose another number:"))
    break
if Operation != "+" and Operation != "-" and Operation != "/" and Operation != "*":
     m = 1
     error==True
while m == 0:
    if Operation == "+":
        s = s + Num3
    elif Operation == "-":
        s = s - Num3
    elif Operation == "/":
        s = s / Num3
    elif Operation == "*":
        s = s * Num3
    print(f"The result is {s}")
    Operation = str(input("Choose the operation. You can choose between +, -, /, *. If you want to end the process press K on your keyboard."))
    if Operation == "k" or Operation == "K":
        m = 1
        K = 1
        break
    if Operation != "+" and Operation != "-" and Operation != "/" and Operation != "*":
        m = 1
        error==True
        break
    Num3 = float(input("Choose another number:"))
if K == 1:
    print("The process has been ended")
if error == True:
    print("There is no such operation!")