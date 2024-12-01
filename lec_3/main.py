def add(a, b):    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")    return a / b

def calculate_expression(tokens):    i = 0
    while i < len(tokens):        if tokens[i] == '*':
            result = multiply(float(tokens[i-1]), float(tokens[i+1]))            tokens = tokens[:i-1] + [result] + tokens[i+2:]
            i -= 1        elif tokens[i] == '/':
            try:                result = divide(float(tokens[i-1]), float(tokens[i+1]))
                tokens = tokens[:i-1] + [result] + tokens[i+2:]                i -= 1
            except ZeroDivisionError as e:                return str(e)
        else:            i += 1
    i = 0
    while i < len(tokens):        if tokens[i] == '+':
            result = add(float(tokens[i-1]), float(tokens[i+1]))            tokens = tokens[:i-1] + [result] + tokens[i+2:]
            i -= 1        elif tokens[i] == '-':
            result = subtract(float(tokens[i-1]), float(tokens[i+1]))            tokens = tokens[:i-1] + [result] + tokens[i+2:]
            i -= 1        else:
            i += 1
    return tokens[0]
def calculator():    print("Enter your calculation (e.g., 5 + 3 - 2 * 4). Type 'quit' to exit.")
    print("Supported operators: +, -, *, /")    
    while True:        user_input = input("\nEnter calculation: ").strip()
        if user_input.lower() == 'quit':            print("Goodbye!")
            break        
        tokens = user_input.split()        
        if not tokens or len(tokens) < 3:            print("Error: Please enter a valid expression with at least two operands and an operator.")
            continue
        try:            result = calculate_expression(tokens)
            print(f"Result: {result}")        except ValueError:
            print("Error: Invalid number or operator in the expression.")        except Exception as e:
            print(f"An unexpected error occurred: {e}")
calculator()
