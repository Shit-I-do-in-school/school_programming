#Vi importar time så vi kan testa hur lång tid det tar att köra genom programmet. import används om man behöver något som t.ex mer matte eller som jag använder time. Då med import math så kan man göra mer avanserad matte med programmet och med import time så kan man göra så att programmet tar tider på hur lång tid en process tar eller så kan du göra att programmet såver med kommandot time.sleep()
import time
#allt ligger i en klass för att jag ville se om det skulle gå (spolier det går)
class Time:
    #Episk felantering
    try:
        #ta in nummeret för första och andra talet
        N,M = int(input("antal siffror i första talet: ")), int(input("antal siffror i andra talet: "))
        #Börja ta tid
        t1 = time.time()
    except:
        print("Det var inte en tal! skriv en tal tack. :)")
        #om talen är mindre en 1 eller större en 9 så slutar vi programmet!
    if not N > 0 and not N < 10 and not M > 0 and not M < 10:
        print("N är utanför gränsen!")
        quit()
#----------------------------------------------------------------
#inte opimalt men det fungerar :)
#Genom att göra på det här sättet så kollar programmet igenom vad vi skriv in för siffra på (N) och kollar från 1-9 och om det skulle vara 7 så skulle den behöva
#gå igenom alla elif tills den kommer till 7 vilket gör att den inte kommer vara lika snabb som om man hade gjort det på nåt annat sätt
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
#----------------------------------------------------------------
#inte opimalt men det fungerar :)
#Genom att göra på det här sättet så kollar programmet igenom vad vi skriv in för siffra på (M) och kollar från 1-9 och om det skulle vara 7 så skulle den behöva
#gå igenom alla elif tills den kommer till 7 vilket gör att den inte kommer vara lika snabb som om man hade gjort det på nåt annat sätt
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
#---------------------------------------------------------------
    #skapar en variabel så vi kan plusa ihop N + M och skriva ut det som braillesiffror
    V = N + M
#----------------------------------------------------------------
#inte opimalt men det fungerar :) använder den nya variabeln för att skriva ut N + M i braille
#Genom att göra på det här sättet så kollar programmet igenom vad vi skriv in för siffra på (N + M) och kollar från 1-9 och om det skulle vara 7 så skulle den behöva
#gå igenom alla elif tills den kommer till 7 vilket gör att den inte kommer vara lika snabb som om man hade gjort det på nåt annat sätt
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
    print(V, "\noch det tog" )
    #sluta ta tid här
    t2 = time.time()
    #printa ut tiden
    print("time = ", t2-t1)