class FormulaError(Exception):
    pass

def calculate(expression):
    parts = expression.split()
    if len(parts) != 3:
        raise FormulaError("Input does not consist of three elements")
    
    try:
        operand1 = float(parts[0])
        operand2 = float(parts[2])
    except ValueError:
        raise FormulaError("The first and third input values must be numbers")
    
    operator = parts[1]
    if operator not in ('+', '-'):
        raise FormulaError("The operator must be '+' or '-'")
    
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2


if __name__ == "__main__":
    while True:
        user_input = input("Enter a calculation (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        try:
            result = calculate(user_input)
            print(f"Result: {result}")
        except FormulaError as e:
            print(f"Error: {e}")