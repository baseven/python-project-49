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


def is_even(num):
    return num % 2 == 0


def get_round_data():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operation_index = random.randint(0, 2)
    operation, symbol = operations[operation_index]
    print(f"symbol {symbol}")
    question = f'Question: {num1} {symbol} {num2}'

    print(f"operation {operation}")

    correct_answer = str(operation(num1, num2))
    print(f"correct_answer {correct_answer}")

    return question, correct_answer


def main():
    engine(game_task, get_round_data)


if __name__ == '__main__':
    main()
