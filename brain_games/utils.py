import random


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


operations = [(add, '+'), (subtract, '-'), (multiply, '*')]


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2)):
        if (num % i) == 0:
            return False
    return True


def get_progression_data():
    first_element = random.randint(0, 10)
    progression_difference = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_element_index = random.randint(0, length - 1)
    hidden_element_symbol = '..'
    progression = []
    elements_count = 0
    while elements_count < length:
        element = first_element + progression_difference * elements_count
        progression.append(str(element))
        elements_count += 1
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = hidden_element_symbol
    return correct_answer, progression
