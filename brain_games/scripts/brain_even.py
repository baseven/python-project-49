import random

from brain_games.game_engine import engine


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_round_data():
    num = random.randint(1, 50)
    question = f'Question: {num}'
    correct_answer = 'yes' if is_even(num) else 'no'
    return question, correct_answer


def main():
    engine(game_task, get_round_data)


if __name__ == '__main__':
    main()
