from brain_games.engine import start_game
from brain_games.games.even import TASK_DESCRIPTION, generate_even_round


def main():
    start_game(TASK_DESCRIPTION, generate_even_round)


if __name__ == "__main__":
    main()