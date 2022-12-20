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

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


