def high_and_low(numbers):
    arr_str = numbers.split()
    min_el = int(arr_str[0])
    max_el = int(arr_str[0])
    for element in arr_str:
        if min_el > int(element):
            min_el = int(element)
        if max_el < int(element):
            max_el = int(element)

    return f"{max_el} {min_el}"


def table_mul(n):
    for i in range(n):
        for j in range(n):
            print((i + 1) * (j + 1), end=' ')
        print("\n")


def no_table_mul(n):
    for i in range(n):
        for j in range(n):
            print(f"{j + 1} * {i + 1} = {(i + 1) * (j + 1)}")


def new_year_mood(n):
    i = 1
    k = 0
    flag = True
    while flag:
        for j in range(i):
            k += 1
            print(k, end=" ")
            if k == n:
                flag = False
                break
        print()
        i += 1


def sum_sum(n):
    sum_number = 0
    for i in range(n):
        sum_number += int(input())
    return sum_number


def hare(n):
    count_hare = 0
    for i in range(n):
        while (string := input()) != "ВСЁ":
            count_hare += 1 if string == "зайка" else 0
    return count_hare


def nod(n):
    nod_number = int(input("Введите число: "))
    for i in range(n-1):
        element = int(input("Введите число: "))
        nod_number, element = element if element < nod_number else nod_number,\
            nod_number if element < nod_number else element
        while nod_number:
            element, nod_number = nod_number, element % nod_number
        nod_number = element
    return nod_number


print(nod(3))
