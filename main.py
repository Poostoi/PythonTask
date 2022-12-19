numbers = input("Введите числа разделённые пробелом")
min = int(numbers[0])
max = int(numbers[0])
for number in numbers:
    if number == " ":
        pass
    elif min > int(number):
        min = int(number)
    elif max < int(number):
        max = int(number)

print(f"{min} {max}")
