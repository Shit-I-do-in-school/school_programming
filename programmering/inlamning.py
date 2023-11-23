#tar in antal ord och vad för mening det är
ord = int(input("Hur många ord? "))
Mening = input("Mening? ")

#vi stripar menigen så vi kan göra den till en lista
naglis = Mening.strip()

#här gör vi listan 🤯🤯🤯🤯🤯🤯
cosmo = list(naglis)

#här gör vi så att orden blir backofram 🤯
cosmo.reverse()

#här gör vi listan till en string igen
s = ''.join(cosmo)

#här tar vi bort korta vokaler :)
s = s.replace('aa', 'å')
s = s.replace('ee', 'e')
s = s.replace('ii', 'i')
s = s.replace('oo', 'o')
s = s.replace('uu', 'u')
s = s.replace('yy', 'y')
#här printar jag svaret!!!!
print(s)