import random

from brain_games.cli import welcome_user


def get_user_name():
    print("Welcome to the Brain Games!")
    user_name = welcome_user("May I have your name? ")
    return user_name


def prepare_game_data(
    numbers_count: int,
    operators_count: int,
    starting_number: int = 1,
    ending_number: int = 100,
):
    available_operators = ["+", "-", "*"]
    operators = []
    for _ in range(operators_count):
        operators.append(random.choice(available_operators))
    numbers = []
    for _ in range(numbers_count):
        number = random.randint(starting_number, ending_number)
        numbers.append(number)
    return {
        "numbers": numbers,
        "operators": operators,
    }


def start_game(expressions, user_name, question_from_func, correct_answer_func):
    for expression in expressions:
        question_text = question_from_func(expression)
        print(f"Question: {question_text}")
        correct_answer = correct_answer_func(expression)
        answer = input("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f'Answer "{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
    return


def main():

    return


if __name__ == "__main__":
    main()
