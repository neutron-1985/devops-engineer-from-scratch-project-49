from brain_games.scripts.brain_games import (
    get_user_name,
    prepare_game_data,
    start_game,
)


def check_even(number):
    return number % 2 == 0


def question_from_func(number):
    return f"{number}"


def correct_answer_func(number):
    return "yes" if check_even(number) else "no"


def main():
    user_name = get_user_name()
    game_data = prepare_game_data(numbers_count=3, operators_count=0)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(
        game_data["numbers"], user_name, question_from_func, correct_answer_func
    )


if __name__ == "__main__":
    main()
