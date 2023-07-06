from operator import add, sub, mul


math_operators = [(add, '+'), (sub, '-'), (mul, '*')]


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2)):
        if (num % i) == 0:
            return False
    return True


def gen_progression(start, step, length):
    progression = []
    elements_count = 0
    while elements_count < length:
        element = start + step * elements_count
        progression.append(str(element))
        elements_count += 1
    return progression


def get_progression_data(start, step, length, missing_index, symbol='..'):
    progression = gen_progression(start, step, length)
    missing_element = progression[missing_index]
    progression[missing_index] = symbol
    return missing_element, progression
