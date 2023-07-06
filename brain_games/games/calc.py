import random

from brain_games.game_engine import engine
from brain_games.utils import math_operators


game_task = 'What is the result of the expression?'


def get_data_for_round():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator, symbol = random.choice(math_operators)
    question = f'Question: {num1} {symbol} {num2}'
    correct_answer = str(operator(num1, num2))
    return question, correct_answer


def run_game():
    engine(game_task, get_data_for_round)
