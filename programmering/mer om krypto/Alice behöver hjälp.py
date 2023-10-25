letter_map = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '10': 'j',
    '11': 'k',
    '12': 'l',
    '13': 'm',
    '14': 'n',
    '15': 'o',
    '16': 'p',
    '17': 'q',
    '18': 'r',
    '19': 's',
    '20': 't',
    '21': 'u',
    '22': 'v',
    '23': 'w',
    '24': 'x',
    '25': 'y',
    '26': 'z',
    '27': 'å',
    '28': 'ä',
    '29': 'ö'
}

input_number = '1121222919'
list = []
def generate_combinations(number, index=0, current_combination=''):
    if index == len(number):
        print(current_combination)
        if not current_combination in list:
            list.append(current_combination)
        return

    if index + 1 < len(number) and number[index:index + 2] in letter_map:
        letter = letter_map[number[index:index + 2]]
        generate_combinations(number, index + 2, current_combination + letter)

    letter = letter_map[number[index]]
    generate_combinations(number, index + 1, current_combination + letter)

generate_combinations(input_number)
print("antal möjliga kombinationer: ", len(list))