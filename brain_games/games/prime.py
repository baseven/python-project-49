import random

from brain_games.game_engine import engine


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2)):
        if (num % i) == 0:
            return False
    return True


def get_round_data():
    num = random.randint(1, 50)
    question = f'Question: {num}'
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


def run_game():
    engine(game_task, get_round_data)
