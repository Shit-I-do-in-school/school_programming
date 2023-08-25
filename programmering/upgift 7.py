#
tal = int(input("Ditt tal: "))

# Skapa en lista med 10 heltal enligt beskrivet mönster
num_list = [tal]
for _ in range(9):
    num_list.append(num_list[-1] * 2)

# Beräkna summan av talen
total_sum = sum(num_list)

print("Listan med heltal:", num_list)

