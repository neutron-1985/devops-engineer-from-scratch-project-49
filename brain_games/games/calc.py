import secrets

TASK_DESCRIPTION = "What is the result of the expression?"


def generate_calc_round(starting_number=1, ending_number=10):
    number1 = secrets.randbelow(
        ending_number - starting_number + 1
        ) + starting_number
    number2 = secrets.randbelow(
        ending_number - starting_number + 1
        ) + starting_number
    operator = secrets.choice(["+", "-", "*"])

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