from brain_games.scripts.brain_calc import main as calc_main
from brain_games.scripts.brain_even import main as even_main
from brain_games.scripts.brain_gcd import main as gcd_main

GAMES = {
    1: ("even", even_main),
    2: ("calc", calc_main),
    3: ("gcd", gcd_main),
}


def choose_game():
    print("Please choose a game:")
    for game_id, (game_name, _) in GAMES.items():
        print(f"{game_id}. {game_name}")

    while True:
        try:
            choice = int(input(
                "Enter the number of the game you want to play: "
                )
            )
            if choice in GAMES:
                _, game_main = GAMES[choice]
                game_main()
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    choose_game()


if __name__ == "__main__":
    main()