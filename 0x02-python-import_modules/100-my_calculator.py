#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    #get argument length
    arg_length = len(sys.argv)

    #check if argument is more than 3
    if arg_length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    #casting a, b into int
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    #checking the operators
    if operator == "+":
        print("{} {} {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{} {} {}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{} {} {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
