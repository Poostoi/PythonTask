def square_numbers(a, b):
    return [i ** 2 for i in range(a, b + 1)]


def table_mul(n):
    return [[(i + 1) * (k + 1) for i in range(n)] for k in range(n)]


def length_word(sentence):
    return [len(i) for i in sentence.split()]


def set_odd(numbers):
    return set([i for i in numbers if i % 2 != 0])


print(set_odd([1, 2, 3,1,43,3,3, 56, 43]))
