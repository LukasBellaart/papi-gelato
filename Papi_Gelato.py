print("Welkom bij Papi Gelato")

gekochtArray = []
prijsArray = { #Prijzen van de pizzas in een dictionary
    "bolletje": 1.10,
    "hoorntje": 1.25,
    "bakje": 0.75
}
def stap1():
    bolletjes = int(input('Hoeveel bolletjes wilt u? -> '))
    if bolletjes >= 1 and bolletjes <= 3:
        for x in range(0, bolletjes):
            gekochtArray.append("bolletje") 
        gekochtArray.append("hoorntje")
        stap2(bolletjes)
    elif bolletjes >=4 and bolletjes <= 8:
        print('Dan krijgt u van mij een bakje met '+ str(bolletjes)+' bolletjes')
        for x in range(0, bolletjes): 
            gekochtArray.append("bolletje")
        gekochtArray.append('bakje')
        stap3(bolletjes, "bakje")
    elif bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet')
        stap1()
    else:
        print("Sorry dat snap ik niet...")
        stap1()

def stap2(bolletjes):
    antwoord = input("Wilt u deze" +  str(bolletjes) + " bolletje(s) in A) een hoorntje of B) een bakje? -> ").lower()
    if antwoord == 'a':
        stap3(bolletjes, "hoorntje")
    elif antwoord == 'b':
        stap3(bolletjes, "bakje")
    else:
        print("Sorry, dat snap ik niet...")
        stap2(bolletjes)

def stap3(bolletjes, hoorntjeOfBakje):
    for i in range(1,bolletjes+1):
        smaak = input('Welke smaak wilt u voor bolletje nummer '+str(i)+'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? -> ').lower()
        if smaak == 'a' or smaak == 'c' or smaak == "m" or smaak == 'v':
            # do nothing
            print('')
        else:
            print("Sorry, dat snap ik niet...")
            stap3(bolletjes, hoorntjeOfBakje)

    antwoord = input("Hier is uw "+hoorntjeOfBakje+" met "+str(bolletjes)+" bolletje(s). Wilt u nog meer bestellen? (Y/N) -> ")
    if antwoord == 'y':
        stap1()
    elif antwoord == 'n':
        bolletjeCount = 0
        hoorntjesCount = 0
        bakjesCount = 0
        for x in gekochtArray: 
            if x == "bolletje":
                bolletjeCount += 1
            elif x == "hoorntje":
                hoorntjesCount += 1
            elif x == "bakje":
                bakjesCount += 1

        print(" ----------------------------------------------------")
        print("Bolletjes       "+str(bolletjeCount)+" x €"+str(prijsArray["bolletje"])+"     = €"+str(bolletjeCount * prijsArray["bolletje"]))
        if hoorntjesCount > 0:
            print("Horrentje       "+str(hoorntjesCount)+" x €"+str(prijsArray["hoorntje"])+"    = €"+str(hoorntjesCount * prijsArray["hoorntje"]))
        if bakjesCount > 0:
            print("Bakje           "+str(bakjesCount)+" x €"+str(prijsArray["bakje"])+"     = €"+str(bakjesCount * prijsArray["bakje"]))      
        print("                             -------- +")   
        print("Totaal                       = €"+str(bolletjeCount * prijsArray["bolletje"] + hoorntjesCount * prijsArray["hoorntje"] + bakjesCount * prijsArray["bakje"]))   

    else:
        print("Sorry, dat snap ik niet...")
        stap3(bolletjes, hoorntjeOfBakje)
stap1()