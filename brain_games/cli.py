import prompt


def welcome_user(text):
    name = prompt.string(text)
    print(f"Hello, {name}!")
    return name
