"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


if __name__ == "__main__":
    while True:
        number1 = int(input("Please Enter Number 1:"))
        number2 = int(input("Please Enter Number 2:"))

        print(add(number1, number2))
        print(subtract(number1, number2))
        print(multiply(number1, number2))
