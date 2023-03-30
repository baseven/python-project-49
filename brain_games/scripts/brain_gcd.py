import math
import random

from brain_games.game_engine import engine


game_task = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    question = f'Question: {num1} {num2}'
    correct_answer = math.gcd(num1, num2)
    return question, str(correct_answer)


def main():
    engine(game_task, get_round_data)


if __name__ == '__main__':
    main()
