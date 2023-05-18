import random

from brain_games.game_engine import engine


game_task = 'What is the result of the expression?'


def custom_sum(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2


operations = [(custom_sum, '+'), (subtract, '-'), (multiply, '*')]


def get_round_data():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operation_index = random.randint(0, 2)
    operation, symbol = operations[operation_index]
    question = f'Question: {num1} {symbol} {num2}'
    correct_answer = str(operation(num1, num2))
    return question, correct_answer


def run_game():
    engine(game_task, get_round_data)
