from brain_games.cli import (
    get_user_answer,
    show_correct_answer,
    show_wrong_answer,
    welcome_user,
)

ROUNDS_COUNT = 3


def get_user_name():
    print("Welcome to the Brain Games!")
    user_name = welcome_user("May I have your name? ")
    return user_name


def generate_rounds(generate_round):
    for _ in range(ROUNDS_COUNT):
        yield generate_round()


def start_game(task_description, generate_round):
    user_name = get_user_name()
    print(task_description)

    rounds = generate_rounds(generate_round)

    for question, correct_answer in rounds:
        print(f"Question: {question}")
        answer = get_user_answer()

        if answer == correct_answer:
            show_correct_answer()
        else:
            show_wrong_answer(answer, correct_answer, user_name)
            return

    print(f"Congratulations, {user_name}!")