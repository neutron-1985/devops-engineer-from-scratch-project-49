from brain_games.engine import start_game
from brain_games.games.calc import TASK_DESCRIPTION, generate_calc_round


def main():
    start_game(TASK_DESCRIPTION, generate_calc_round)


if __name__ == "__main__":
    main()