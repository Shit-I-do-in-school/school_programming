#uppgift 6

votes = []
y = 0.0
for i in range(1,8):
    votes.append(float(input(f"Domaren nr. {i}: ")))

votes.sort()
votes.pop(0)
votes.pop(4)
#printa ut svar
print("Medelvärdet är:", round(sum(votes)/len(votes),2))