# # ------- First Task
# list_word = input()
# list_format = [f"{index}. {value}" for index, value in enumerate(list_word.split(" "), 1)]
#
# [print(i) for i in list_format]
# -------- Second Task
first_row = input()
second_row = input()
[print(f"{i[0]} - {i[1]}") for i in zip(first_row.split(", "), second_row.split(", "))]
