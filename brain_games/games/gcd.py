import secrets

TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_gcd_round():
    number1 = secrets.randbelow(100) + 1
    number2 = secrets.randbelow(100) + 1
    question = f"{number1} {number2}"
    correct_answer = find_gcd(number1, number2)
    return question, str(correct_answer)
