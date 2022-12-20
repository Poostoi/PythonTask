numbers = input("Введите числа разделённые пробелом")


def high_and_low(numbers):
    min = int(numbers[0])
    max = int(numbers[0])
    number = "";
    for i in range(len(numbers)):
        if numbers[i] == '':
            pass
        elif numbers[i] == " ":
            number = ""
            continue
        elif numbers[i + 1] != " ":
            number += numbers[i]
            continue
        number += numbers[i]
        if min > int(number):
            min = int(number)
        else:
            max = int(number)

    return f"{max} {min}"
