def parse_number(matrix):
    matrix = matrix.replace('\n', '')
    return {
        '     |  |': '1',
        '   |_|  |': '4',
        ' _   |  |': '7',
        ' _  _| _|': '3',
        ' _  _||_ ': '2',
        ' _ | ||_|': '0',
        ' _ |_  _|': '5',
        ' _ |_ |_|': '6',
        ' _ |_| _|': '9',
        ' _ |_||_|': '8',
    }[matrix]


def binarize(text):
    return ''.join(
        ['0' if char == ' ' else '1'
         for char
         in text])


def parse_input(text):
    account_number = ''
    text = text.replace('\n', '')
    character_size = 3
    columns = 9 * character_size
    for i in range(0, columns, 3):
        account_number += parse_number(
            text[i:i+character_size]+
            text[i+columns:i+columns+character_size]+
            text[i+(columns)*2:i+((columns)*2)+character_size])
    return account_number
