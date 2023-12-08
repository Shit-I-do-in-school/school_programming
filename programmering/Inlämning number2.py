import time

try:
    #ta in nummeret för första talet
    N = int(input("antal siffror i första talet: "))

    #om talet är mindre en 1 eller större en 9 så slutar vi programmet!
    if not N >= 1 or not N <= 9:
        print("N är utanför gränsen!")
        quit()

    #ta in nummeret för andra talet
    M = int(input("antal siffror i andra talet: "))

    #om talet är mindre en 1 eller större en 9 så slutar vi programmet!
    if not M >= 1 or not M <= 9:
        print("M är utanför gränsen!")
        quit()
    t1 = time.time()
    #Vi gör en klass för att prova nya saker
    class Test:
        if N == 1:
            print(" *. \n .. \n .. ")
        elif N == 2:
            print(" *. \n *. \n .. ")
        elif N == 3:
            print(" ** \n .. \n .. ")
        elif N == 4:
            print(" ** \n .* \n .. ")
        elif N == 5:
            print(" *. \n .* \n .. ")
        elif N == 6:
            print(" ** \n *. \n .. ")
        elif N == 7:
            print(" ** \n ** \n .. ")
        elif N == 8:
            print(" *. \n ** \n .. ")
        elif N == 9:
            print(" .* \n *. \n .. ")
            
    #prinar \n för att få ny rad så jag kan skriva +    
    print(" \n + \n")

    #SAMMA jag gillar klasserna
    class Test2:
        if M == 1:
            print(" *. \n .. \n .. ")
        elif M == 2:
            print(" *. \n *. \n .. ")
        elif M == 3:
            print(" ** \n .. \n .. ")
        elif M == 4:
            print(" ** \n .* \n .. ")
        elif M == 5:
            print(" *. \n .* \n .. ")
        elif M == 6:
            print(" ** \n *. \n .. ")
        elif M== 7:
            print(" ** \n ** \n .. ")
        elif M == 8:
            print(" *. \n ** \n .. ")
        elif M == 9:
            print(" .* \n *. \n .. ")

    #skapar en variabel så vi kan plusa ihop N + M och skriva ut det som braillesiffror
    V = N + M

    #skapar en funktion för hittade inget annant sätt att göra det på med en klass :(
    def Test3():
        
        print(" \n = \n")
        if V == 0:
            print(" .* \n ** \n .. ")
        elif V == 1:
            print(" *. \n .. \n .. ")
        elif V == 2:
            print(" *. \n *. \n .. ")
        elif V == 3:
            print(" ** \n .. \n .. ")
        elif V == 4:
            print(" ** \n .* \n .. ")
        elif V == 5:
            print(" *. \n .* \n .. ")
        elif V == 6:
            print(" ** \n *. \n .. ")
        elif V == 7:
            print(" ** \n ** \n .. ")
        elif V == 8:
            print(" *. \n ** \n .. ")
        elif V == 9:
            print(" .* \n *. \n .. ")
        elif V == 10:
            print(" *. .* \n .. ** \n .. .. ")
        elif V == 11:
            print(" *. *. \n .. .. \n .. .. ")
        elif V == 12:
            print(" *. *. \n .. *. \n .. .. ")
        elif V == 13:
            print(" *. ** \n .. .. \n .. .. ")
        elif V == 14:
            print(" *. ** \n .. .* \n .. .. ")
        elif V == 15:
            print(" *. *. \n .. .* \n .. .. ")
        elif V == 16:
            print(" *. ** \n .. *. \n .. .. ")
        elif V == 17:
            print(" *. ** \n .. ** \n .. .. ")
        elif V == 18:
            print(" *. *. \n .. ** \n .. .. ")

    # kör test 3 så vi kan se vad dem två talen blir tillsammans
    Test3()
    #väldigt onöding except men den ser kool ut
    t2 = time.time()
    print("time = ", t2-t1)
except Exception as e:
    print("Det var en error :(" , e)