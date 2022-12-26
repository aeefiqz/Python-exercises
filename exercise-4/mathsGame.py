import random

def generate_operands(num_digits):
    # generate operands with the specified number of digits
    operand1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
    operand2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
    return operand1, operand2

def getOperator():
    # Generate a random number between 0 and 2
    operator = random.randint(0, 2)
    # Return the operator corresponding to the random number
    if operator == 0:
        return "+"
    elif operator == 1:
        return "-"
    else:
        return "*"

def generate_subtraction_operands(num_digits):
      # generate operands for subtraction where the second operand is always less than the first
    operand1, operand2 = generate_operands(num_digits)
    while operand2 > operand1:
        operand1, operand2 = generate_operands(num_digits)
    return operand1, operand2

def generate_multiplication_operands(num_digits):
    operand1, operand2 = generate_operands(num_digits)
    # for multiplication, the first operand should not start with 1
    while operand1 < 10:
        operand1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
        operand2 = random.randint(2, 9)

    return operand1, operand2

def getExpression(level, operator):
    # generate operands based on the level and operator
    num_digits =  level + 1  # number of digits for the operands
    operand1 = 0
    operand2 = 0
    if operator == '*':
        operand1, operand2 = generate_multiplication_operands(num_digits)
    elif operator == '-':
        # for subtraction, generate operands where the second operand is always less than the first
        operand1, operand2 = generate_subtraction_operands(num_digits)
    else:
        # for addition, generate operands with the specified number of digits
        operand1, operand2 = generate_operands(num_digits)

    # create the expression string and calculate the result
    expression = f"{operand1} {operator} {operand2} = "
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2

    return expression, result



    
def main():
    highest_level = int(input("Enter highest level to achieve (1-5): "))
    while 0 < highest_level > 6:
        print("Highest level must be between 1 and 5")
        highest_level = int(input("Enter highest level to achieve (1-5): "))
    
    current_level = 1
    
    while current_level <= highest_level: 
        print(f"Level {current_level}")
        errors = 0
        correct_answer = 0
        while errors < 1:
            for _ in range(3):
                operator = getOperator()
                expression, result = getExpression(current_level, operator)
                print(expression, sep='',end='')
                answer = int(input())
                if answer == result:
                    print(f"Correct!")
                    correct_answer += 1
                else:
                    print(f"Wrong! Answer is {result}")
                    errors += 1
            if errors > 1 :
                print(f"You have {errors} error, press <ENTER> to repeat the level: ",sep='',end='')
                input()
            else:
                current_level += 1
                print(f"Well done! Press <ENTER> to proceed to level {current_level}: ", sep='', end='')
                input()
        
    print(f"Well Done! You have completed the highest level {highest_level}")
main()