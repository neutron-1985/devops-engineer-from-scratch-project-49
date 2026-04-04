from brain_games.engine import start_game
from brain_games.games.prime import TASK_DESCRIPTION, generate_prime_round


def main():
    start_game(TASK_DESCRIPTION, generate_prime_round)


if __name__ == "__main__":
    main()