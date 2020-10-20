Airthmatic operations using functions

num1=int(input("Enter first number: "))
num2=int(input("Enter Second number: "))
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print(""" Enter your choice from below
            Press 1 for Addition
            Press 2 for Subtraction
            Press 3 for Multiplication
            Press 4 for Division""")
choice=int(input())
print(choice)
if choice not in range(1,5):
    print("Enter Operation number correctly")
else:
    if choice==1:
        print(f'Addition of {num1} and {num2} is {add(num1,num2)}')
    if choice==2:
        print(f'Subtraction of {num1} and {num2} is {sub(num1,num2)}')
    if choice==3:
        print(f'Multiplication of {num1} and {num2} is {mul(num1,num2)}')
    if choice==4:
        print(f'Division of {num1} and {num2} is {div(num1,num2)}')