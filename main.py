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
    table = [[0] * n] * n;
    for i in range(n):
        for j in range(n):
            table[i][j] = i * j
    return table

print(table_mul(5))
m = [range(5)]
print(m)
