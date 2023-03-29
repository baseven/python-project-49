import prompt
import random

game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
success_message = 'Congratulations, <user_name>!'
error_message = "'<answer>' is wrong answer ;(. " \
                "Correct answer was '<correct_answer>'.\n" \
                "Let's try again, <user_name>!"


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(num):
    return num % 2 == 0


def run_game():
    user_name = welcome_user()
    print(game_rule)
    answers_count = 0
    while answers_count < 3:
        num = random.randint(1, 50)
        correct_answer = 'yes' if is_even(num) else 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            answers_count += 1
        else:
            error_msg = error_message\
                .replace('<answer>', answer)\
                .replace('<correct_answer>', correct_answer)\
                .replace('<user_name>', user_name)
            print(error_msg)
            break
        if answers_count == 3:
            print(success_message.replace('<user_name>', user_name))


def main():
    run_game()


if __name__ == '__main__':
    main()
