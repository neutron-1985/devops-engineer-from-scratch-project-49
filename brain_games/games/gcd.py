import random

TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_gcd_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = find_gcd(number1, number2)
    return question, str(correct_answer)
