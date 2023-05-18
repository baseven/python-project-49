import random

from brain_games.game_engine import engine
from brain_games.utils import is_prime


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_data_for_round():
    num = random.randint(1, 50)
    question = f'Question: {num}'
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


def run_game():
    engine(game_task, get_data_for_round)
