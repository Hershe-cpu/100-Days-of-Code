print("""
 _____________________
|  _________________  |
| | Harshita     0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

""")
x=0
def calculator(num1,num2,operation):
    
    if operation=="+":
        return (num1+num2)
    elif operation=="-":
        return (num1-num2)
    elif operation=="*":
        return (num1*num2)
    elif operation=="/":
        return (num1/num2)
    else:
       print("Invalid operation")
       return None


n1=float(input("What's the first number?: "))
calculation_finished=False
while not calculation_finished:
    print("+")
    print("-")
    print("*")
    print("/")
    oper=input("Pick an operation: ")
    n2=float(input("What's the next number?: "))
    result = calculator(n1,n2,oper)
    if result is not None:
        print(f"{n1} {oper} {n2} = {result} " )
    yn=input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation: ")
    if yn=="y":
        n1=result
    else:
        calculation_finished=True