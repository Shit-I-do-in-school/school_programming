<<<<<<< HEAD

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
=======
s1 = int(input("Antal ettor: "))
s2 = int(input("Antal tvÃ¥or: "))
s3 = int(input("Antal treor: "))
s4 = int(input("Antal fyror: "))

team1 = 0
team2 = 0
team1list = [0,0,0,0]
team2list = [0,0,0,0]

while s1 > 0:
    if s1 % 2 == 0:#0 = no remainder
        team1 +=1
        s1 -= 1
        team1list[0] += 1
    else:
        team2 +=1
        s1 -= 1
        team2list[0] += 1
while s2 > 0:
    if s2 % 2 == 0:
        team1 +=2
        s2 -= 1
        team1list[1] += 1
    else:
        team2 +=2
        s2 -= 1
        team2list[1] += 1
while s3 > 0:
    if s3 % 2 == 0:
        team1 +=3
        s3 -= 1
        team1list[2] += 1
    else:
        team2 +=3
        s3 -= 1
        team2list[2] += 1
while s4 > 0:
    if s4 % 2 == 0:
        team1 +=4
        s4 -= 1
        team1list[3] += 1
    else:
        team2 +=4
        s4 -= 1
        team2list[3] += 1

while team1 != team2:
    if team1 > team2:#fr[n 1 till 2
        if team1list[0] > 0:
            team1list[0] -= 1
            team2list[0] += 1
            team1 -= 1
            team2 += 1
        elif team1list[1] > 0:
            team1list[1] -= 1
            team2list[1] += 1
            team1 -= 2
            team2 += 2
        elif team1list[2] > 0:
            team1list[2] -= 1
            team2list[2] += 1
            team1 -= 3
            team2 += 3
        elif team1list[3] > 0:
            team1list[3] -= 1
            team2list[3] += 1
            team1 -= 4
            team2 += 4
        else:
            break
    elif team2 > team1:  # fr[n 2 till 1
        if team2list[0] > 0:
            team2list[0] -= 1
            team1list[0] += 1
            team2 -= 1
            team1 += 1
        elif team2list[1] > 0:
            team2list[1] -= 1
            team1list[1] += 1
            team2 -= 2
            team1 += 2
        elif team2list[2] > 0:
            team2list[2] -= 1
            team1list[2] += 1
            team2 -= 3
            team1 += 3
        elif team2list[3] > 0:
            team2list[3] -= 1
            team1list[3] += 1
            team2 -= 4
            team1 += 4
        else:
            break

print("Team 1: ", team1list)
print("Team 2: ", team2list)
>>>>>>> 7822b087e88dcd91deaf64df3c902a33fd6707f9
