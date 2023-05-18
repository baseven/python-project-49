import random

from brain_games.game_engine import engine
from brain_games.utils import get_progression_data

game_task = 'What number is missing in the progression?'


def get_data_for_round():
    first_element = random.randint(0, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    missing_index = random.randint(0, length - 1)
    progression_data = get_progression_data(start=first_element,
                                            step=step,
                                            length=length,
                                            missing_index=missing_index)
    correct_answer, progression = progression_data
    question = f'Question: {" ".join(progression)}'
    return question, str(correct_answer)


def run_game():
    engine(game_task, get_data_for_round)
