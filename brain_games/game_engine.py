import prompt

success_message = 'Congratulations, <user_name>!'
error_message = "'<answer>' is wrong answer ;(. " \
                "Correct answer was '<correct_answer>'.\n" \
                "Let's try again, <user_name>!"

rounds_number = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine(game_task, get_round_data):
    user_name = welcome_user()
    print(game_task)
    round_count = 0
    while round_count < rounds_number:
        question, correct_answer = get_round_data()
        print(question)
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            round_count += 1
        else:
            error_msg = error_message\
                .replace('<answer>', answer)\
                .replace('<correct_answer>', correct_answer)\
                .replace('<user_name>', user_name)
            print(error_msg)
            break
        if round_count == rounds_number:
            print(success_message.replace('<user_name>', user_name))
