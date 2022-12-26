def valid_Expression(expression):
    #split the expression into individual tokens
    tokens = expression.split()

    if len(tokens) != 3:
        return "Invalid number of tokens"

    # Check if the first and last tokens are binary strings of the same length
    operand1 = tokens[0]
    operand2 = tokens[2]
    if not all(x in '01' for x in operand1):
        print("First operand is not a binary string" )
        return False
    if not all( x in '01' for x in operand2):
        print("Second operand is not a binary string")
        return False
    if len(operand1) != len(operand2):
        print("Operands are of different length")
        return False

    operator = tokens[1]
    if operator not in ['&','|','^']:
        print("Invalid operator")
        return False
    
    return True

def evaluate_binary_expression(expression):
    # Split the expression into individual tokens
    tokens = expression.split()

    # Get the operands and operator
    operand1 = tokens[0]
    operator = tokens[1]
    operand2 = tokens[2]

    # Initialize a result string
    result = ''

    # Iterate through the operands and perform the bitwise operation
    for i in range(len(operand1)):
        bit1 = int(operand1[i])
        bit2 = int(operand2[i])
        if operator == '&':
            result += str(bit1 & bit2)
        elif operator == '|':
            result += str(bit1 | bit2)
        elif operator == '^':
            result += str(bit1 ^ bit2)

    result_str = ''
    result_str += ' ' + operand1 + '\n'
    result_str += ' ' * (len(operand1) - len(operator)) + operator + ' ' + operand2 + '\n'
    result_str += '-' * len(operand1) + '\n'
    result_str += ' ' * (len(operand1) - len(result)) + result

    # Return the result
    return result_str

def main():
    while True:
        expression = input("Enter binary expression: ")
        if expression == "":
            break
        if valid_Expression(expression):
            result = evaluate_binary_expression(expression)
            print(result)
    print(f"End of program")
main()

