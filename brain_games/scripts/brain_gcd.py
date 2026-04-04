from brain_games.engine import start_game
from brain_games.games.gcd import TASK_DESCRIPTION, generate_gcd_round


def main():
    start_game(TASK_DESCRIPTION, generate_gcd_round)


if __name__ == "__main__":
    main()