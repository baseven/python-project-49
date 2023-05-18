from brain_games.game_engine import engine
from brain_games.utils import get_progression_data


game_task = 'What number is missing in the progression?'


def get_data_for_round():
    correct_answer, progression = get_progression_data()
    question = f'Question: {" ".join(progression)}'
    return question, str(correct_answer)


def run_game():
    engine(game_task, get_data_for_round)
