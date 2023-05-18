import random

from brain_games.game_engine import engine


game_task = 'What number is missing in the progression?'


def gen_progression():
    first_element = random.randint(0, 10)
    difference = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_element_index = random.randint(0, length - 1)
    hidden_element_symbol = '..'
    progression = []
    elements_count = 0
    while elements_count < length:
        element = first_element + difference * elements_count
        progression.append(str(element))
        elements_count += 1
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = hidden_element_symbol
    return correct_answer, progression


def get_data_for_round():
    correct_answer, progression = gen_progression()
    question = f'Question: {" ".join(progression)}'
    return question, str(correct_answer)


def run_game():
    engine(game_task, get_data_for_round)
