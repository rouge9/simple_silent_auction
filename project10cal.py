def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operator={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
    }


def calculator():
    num1 = int(input("insert first number"))
    for symbol in operator:
        print(symbol)
    run = True
    while run == True:
        operator_symbol = input("insert operator")
        num2 = int(input("insert second number"))
        calculate = operator[operator_symbol]
        answer = calculate(num1,num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")

        flag = input("press 'y' to continue if not press 'n' to continue press 'c'")
        if flag == "y":
            num1 = answer
        elif flag == "c":
            calculator()


calculator()
