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


print(new_year_mood(5))
