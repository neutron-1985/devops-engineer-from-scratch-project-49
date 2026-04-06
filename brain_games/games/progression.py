import secrets

TASK_DESCRIPTION = 'What number is missing in the progression?'


def generate_progression_round():
    start = secrets.randbelow(10) + 1
    step = secrets.randbelow(10) + 1
    length = secrets.randbelow(6) + 5
    progression = [start + i * step for i in range(length)]
    missing_index = secrets.randbelow(length)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
