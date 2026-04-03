import random

from brain_games.scripts.brain_games import main as main_game


def main_task(user_name):
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(question)
    numbers = []
    for _ in range(3):
        number = random.randint(1, 100)
        numbers.append(number)
    for number in numbers:
        correct_answer = 'yes' if check_even(number) else 'no'
        print(f'Question: {number}')
        answer = input("Your answer: ")
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"Answer \"{answer}\" is wrong answer ;(. "
                f"Correct answer was \"{correct_answer}\"."
            )
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
    return


def check_even(number):
    return number % 2 == 0


def main():
    user_name = main_game()
    main_task(user_name)


if __name__ == '__main__':
    main()