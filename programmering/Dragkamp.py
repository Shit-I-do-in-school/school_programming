s1 = int(input("Antal ettor: "))
s2 = int(input("Antal tvåor: "))
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