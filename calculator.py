import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def calculator():
    print(logo.logo)
    should_accumulate = True
    n1 = input("What's the first number?")
    while should_accumulate:
        operator = input("+\n"
                         "-\n"
                         "*\n"
                         "/\n"
                         "Pick an operation: ")
        n2 = input("What's the next number?")
        float(n1)
        float(n2)
        calculation = (operations[operator](float(n1), float(n2)))
        print(f"{n1} {operator} {n2} = {calculation}")
        choice = (input(f"Type 'y' if you would like to continue calculating with {calculation}, or type 'n' if you would like to start a new calculation: "))
        if choice == "y":
            n1 = calculation
        if choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()