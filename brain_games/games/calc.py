import random

from brain_games.game_engine import engine


game_task = 'What is the result of the expression?'


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


operations = [(add, '+'), (subtract, '-'), (multiply, '*')]


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
