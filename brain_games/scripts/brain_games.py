from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user('May I have your name? ')
    return user_name


if __name__ == '__main__':
    main()