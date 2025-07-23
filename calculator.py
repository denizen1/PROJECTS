def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
def calculator():
    should_accumulate = True
    num1= float(input("What is your first number?: "))
    while should_accumulate:
    
        for symbol in operations:
            print(symbol)
            operations_symbol = input("Pick an operations: ")
            num2= float(input("What is your second number?: "))
            answer= operations[operations_symbol](num1, num2)

            print(f"{num1} {operations} {num2} = {answer}")

            choice = input(f"Type y to continue calculating with {answer}, or type n to start new calculation")

            if choice == "y":
                num1= answer
            else:
                should_accumulate = False
                print("\n" * 20)
                calculator()

calculator()