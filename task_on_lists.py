def check_first_char(n):
    list_words = [input() for i in range(n)]
    for element in list_words:
        if element[0].lower() != "а" and element[0].lower() != "б" and element[0].lower() != "в":
            return 'NO'
    return 'YES'


def flip_line(line):
    invert_line = ''
    for char_from_line in line:
        invert_line += char_from_line + '\n'
    return invert_line


def clip_title():
    n = int(input())
    length_str = int(input())
    list_title = [input() for i in range(n)]
    result_title = ''
    for title in list_title:
        if len(title) > length_str:
            result_title += title[:length_str] + '\n'
    return result_title


print(clip_title())
