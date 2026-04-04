import random

TASK_DESCRIPTION = "What is the result of the expression?"


def generate_calc_round(starting_number=1, ending_number=10):
    number1 = random.randint(starting_number, ending_number)
    number2 = random.randint(starting_number, ending_number)
    operator = random.choice(["+", "-", "*"])

    question = f"{number1} {operator} {number2}"
    correct_answer = calculate(number1, number2, operator)

    return question, str(correct_answer)


def calculate(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2