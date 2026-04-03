from brain_games.scripts.brain_games import (
    get_user_name,
    prepare_game_data,
    start_game,
)


def generate_expression(numbers, operators):
    expressions = []
    for i in range(len(operators)):
        expressions.append([numbers[i * 2], operators[i], numbers[i * 2 + 1]])
    return expressions


def question_from_func(expression):
    return f"{expression[0]} {expression[1]} {expression[2]}"


def correct_answer_func(expression):
    return str(eval(f"{expression[0]} {expression[1]} {expression[2]}"))


def main():
    user_name = get_user_name()
    game_data = prepare_game_data(
        numbers_count=6, operators_count=3, ending_number=10
    )
    expressions = generate_expression(
        game_data["numbers"], game_data["operators"]
    )
    print("What is the result of the expression?")

    start_game(expressions, user_name, question_from_func, correct_answer_func)


if __name__ == "__main__":
    main()
