import art

def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
}
while True:
    print(art.logo)
    first_number = float(input("whats the first number? : "))
    operation = input("+\n*\n/\n-\npick an operation : ")
    second_number = float(input("whats the second number? : "))
    result = 0
    while True:
        result = operations[operation](first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        continue_check = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continue_check == "y":
            first_number = result
            operation = input("+\n*\n/\n-\npick an operation : ")
            second_number = float(input("whats the second number? : "))
        else:
            print("\n" * 50)
            break




