"""This is a simple calculator. It adds, subtracts, multiplies, or 
divides two numbers. The required form of input is e.g.: "1 + 2".
It shows error messages when entering wrong input. The calculator
asks for input until the user hits enter."""

def addition(a,b):
    return a+b


def subtraction(a,b):
    return a-b


def multiplication(a,b):
    return a*b


def division(a,b):
    return a/b


def answer(a,b,operator):
    """The function decides which operator should be used and
    returns the right answer."""

    if operator == "+":
        return addition(a,b)
    
    if operator == "-":  
        return subtraction(a,b)
    
    if operator == "*":  
        return multiplication(a,b)
    
    if operator == "/":
        return division(a,b)

    return "false"


def main():
    print("Hello! Enter a calculation in following form:\n<number1><space><operator><space><number2>\n")
    example = " "
    
    while example != "":
        example = input("Enter an example: ")
        
        if example != "":
            try:
                example_splitted = example.split()

                if len(example_splitted) > 4: # too many arguments in the output
                    print("TooManyArguments: {0} contains too many operations".format(example))
                    print("Please, enter only two numbers and an operator: <number1><space><operator><space><number2>")
                    continue

                if example_splitted[2] == "-0": # division by minus zero
                    print("Answer: -Infinity")
                    continue

                if example_splitted[2] == "0": # division by zero
                    print("Answer: Infinity")
                    continue
                
                a = float(example_splitted[0]) # first number
                b = float(example_splitted[2]) # second number
                ans = answer(a, b, example_splitted[1]) # example_splitted[1] is the operator
                
                if ans == "false": # wrong operator
                    print("WrongOperator: the operator you selected is not valid")
                    print("Please, enter only valid operator: + - * /")
                else:
                    print("Answer: ", ans)

            except ValueError:
                print("ValueError: {0} doesn't contain numbers".format(example))
                print("Please, enter two numbers and an operator: <number1><space><operator><space><number2>")
            
            except IndexError:
                print("IndexError: {0} is missing operator or incorrect format".format(example))
                print("Please, enter two numbers and an operator: <number1><space><operator><space><number2>")

        if example == "":
            print("Bye!")

main()    
