import prompt


def welcome_user(text):
    name = prompt.string(text)
    print(f"Hello, {name}!")
    return name


def get_user_answer():
    answer = prompt.string("Your answer: ")
    return answer


def show_correct_answer():
    print("Correct!")
    

def show_wrong_answer(user_answer, correct_answer, user_name):
    print(
        f'Answer "{user_answer}" is wrong answer ;(. '
        f'Correct answer was "{correct_answer}".'
    )
    print(f"Let's try again, {user_name}!")