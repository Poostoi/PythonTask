import math


def square_numbers(a, b):
    return [i ** 2 for i in range(a, b + 1)]


def table_mul(n):
    return [[(i + 1) * (k + 1) for i in range(n)] for k in range(n)]


def length_word(sentence):
    return [len(i) for i in sentence.split()]


def set_odd(numbers):
    return set([i for i in numbers if i % 2 != 0])


def find_square(numbers):
    return set([i for i in numbers if math.sqrt(i) % 1 == 0])


def count_letters(text):
    return {elem: text.lower().count(elem) for elem in set(text.lower())}


def find_all_divisors(numbers):
    return {elem: [i for i in range(1, elem + 1) if elem % i == 0] for elem in numbers}


print(find_all_divisors({1, 2, 3, 4, 5}))
