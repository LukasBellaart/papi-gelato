print("Welkom bij Papi Gelato")

gekochtArray = []
prijsArray = { #Prijzen van de pizzas in een dictionary
    "bolletje": 1.10,
    "hoorntje": 1.25,
    "bakje": 0.75,
    'slagroom': 0.50,
    'sprinkels': 0.30,
    'caramelBakje':0.90,
    'caramelHoorntje':0.60,
    'liter':9.80
}

BTW = 9

def particulierOfZakelijk():
    while True:
        particulierOfZakelijk = input('Bent u 1) particulier of 2) zakelijk? -> ')

        if particulierOfZakelijk == "1":
            return stap1()
        elif particulierOfZakelijk == "2":
            return stap1Zakelijk()
        else:
            print("Sorry dat snap ik niet...")
            


def stap1Zakelijk():
    liter = int(input('Hoeveel liter wilt u? -> '))
    if liter >= 1 and liter <= 3:
        for x in range(0, liter):
            gekochtArray.append("liter") 
        stap2Zakelijk(liter)
    else:
        print("Sorry dat snap ik niet...")
        stap1Zakelijk()

def stap2Zakelijk(liters):
    for i in range(1,liters+1):
        smaak = input('Welke smaak wilt u voor liter '+str(i)+'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? -> ').lower()
        if smaak == 'a' or smaak == 'c' or smaak == "m" or smaak == 'v':
            # do nothing
            print('')
        else:
            print("Sorry, dat snap ik niet...")
            stap2Zakelijk(liters)
    
    liter = 0
    for x in gekochtArray: 
        if x == "liter":
            liter += 1


    print(" ----------------------------------------------------")
    print("Liter       "+str(round(liter,2))+" x €"+str(round(prijsArray["liter"],2))+"     = €"+str(round(liter * prijsArray["liter"],2)))
    print("                             -------- +")   
    print("Totaal                       = €"+str(round(liter * prijsArray["liter"],2)))   
    print("BTW                       = €"+str(round(BTW * (liter * prijsArray["liter"])/100,2)))

# def percentage(percent, whole):
#   return (percent * whole) / 100.0



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
    antwoord = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? -> ").lower()
    if antwoord == 'a':
        stap4(bolletjes, hoorntjeOfBakje)
    elif antwoord == 'b':
        gekochtArray.append('slagroom')
        stap4(bolletjes, hoorntjeOfBakje)
    elif antwoord == 'c':
        gekochtArray.append('sprinkels')
        stap4(bolletjes, hoorntjeOfBakje)
    elif antwoord == 'd':
        gekochtArray.append('caramel')
        if hoorntjeOfBakje == "bakje":
            gekochtArray.append('caramelBakje')
        else:
            gekochtArray.append('caramelHoorntje')


        stap4(bolletjes, hoorntjeOfBakje)
    else:
        print("Sorry, dat snap ik niet...")
        stap3(bolletjes)

def stap4(bolletjes, hoorntjeOfBakje):
    for i in range(1,bolletjes+1):
        smaak = input('Welke smaak wilt u voor bolletje nummer '+str(i)+'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? -> ').lower()
        if smaak == 'a' or smaak == 'c' or smaak == "m" or smaak == 'v':
            # do nothing
            print('')
        else:
            print("Sorry, dat snap ik niet...")
            stap4(bolletjes, hoorntjeOfBakje)

    antwoord = input("Hier is uw "+hoorntjeOfBakje+" met "+str(bolletjes)+" bolletje(s). Wilt u nog meer bestellen? (Y/N) -> ")
    if antwoord == 'y':
        stap1()
    elif antwoord == 'n':
        bolletjeCount = 0
        hoorntjesCount = 0
        bakjesCount = 0
        slagroom = 0
        sprinkels = 0
        caramelBakje = 0
        caramelHoorntje = 0
        for x in gekochtArray: 
            if x == "bolletje":
                bolletjeCount += 1
            elif x == "hoorntje":
                hoorntjesCount += 1
            elif x == "bakje":
                bakjesCount += 1
            elif x == 'slagroom:':
                slagroom += 1
            elif x == "sprinkels":
                sprinkels += 1
            elif x == "caramelBakje":
                caramelBakje += 1
            elif x == "caramelHoorntje":
                caramelHoorntje += 1

        print(" ----------------------------------------------------")
        print("Bolletjes       "+str(bolletjeCount)+" x €"+str(prijsArray["bolletje"])+"     = €"+str(round(bolletjeCount * prijsArray["bolletje"],2)))
        if hoorntjesCount > 0:
            print("Horrentje       "+str(hoorntjesCount)+" x €"+str(prijsArray["hoorntje"])+"    = €"+str(round(hoorntjesCount * prijsArray["hoorntje"],2)))
        if bakjesCount > 0:
            print("Bakje           "+str(bakjesCount)+" x €"+str(prijsArray["bakje"])+"     = €"+str(round(bakjesCount * prijsArray["bakje"],2)))  
        if slagroom + sprinkels + caramelBakje + caramelHoorntje > 0:
            print("Toppings        "+str(slagroom + sprinkels + caramelBakje + caramelHoorntje)+"             = €"+str(round(slagroom * prijsArray["slagroom"] + sprinkels * prijsArray["sprinkels"] + caramelBakje * prijsArray["caramelBakje"] + caramelHoorntje * prijsArray["caramelHoorntje"],2)))
        print("                             -------- +")   
        print("Totaal                       = €"+str(round(bolletjeCount * prijsArray["bolletje"] + hoorntjesCount * prijsArray["hoorntje"] + bakjesCount * prijsArray["bakje"] + slagroom * prijsArray["slagroom"] + sprinkels * prijsArray["sprinkels"] + caramelBakje * prijsArray["caramelBakje"] + caramelHoorntje * prijsArray["caramelHoorntje"],2)))   

    else:
        print("Sorry, dat snap ik niet...")
        stap4(bolletjes, hoorntjeOfBakje)
particulierOfZakelijk()