import random

from brain_games.game_engine import engine
from brain_games.utils import operations


game_task = 'What is the result of the expression?'


def get_data_for_round():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    random_operation_index = random.randint(0, (len(operations) - 1))
    operation, symbol = operations[random_operation_index]
    question = f'Question: {num1} {symbol} {num2}'
    correct_answer = str(operation(num1, num2))
    return question, correct_answer


def run_game():
    engine(game_task, get_data_for_round)
