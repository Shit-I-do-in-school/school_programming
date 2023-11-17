n = int(input("Antel deltagare: "))#input här
if n < 1 or n > 10000:#kolla antal
    print("Dålig antal deltagare")
    quit()#nej

n1, n2 = 0, 1
count = 0
no = []

while n-sum(no) > 0:#den kollar om någonting
    #fibinaci
    nth = n1 + n2
    n1 = n2
    n2 = nth

    no.append(n1)#lägg till listan
    count += 1

print("Svar: ", count)#print
