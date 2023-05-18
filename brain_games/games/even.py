import random

from brain_games.game_engine import engine
from brain_games.utils import is_even


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_data_for_round():
    num = random.randint(0, 50)
    question = f'Question: {num}'
    correct_answer = 'yes' if is_even(num) else 'no'
    return question, correct_answer


def run_game():
    engine(game_task, get_data_for_round)
