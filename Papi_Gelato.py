print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
def stap1():
    bolletjes = int(input('Hoeveel bolletjes wilt u? -> '))
    if bolletjes >= 1 and bolletjes <= 3:
        stap2(bolletjes)
    elif bolletjes >=4 and bolletjes <= 8:
        print('Dan krijgt u van mij een bakje met '+ str(bolletjes)+' bolletjes')
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
    antwoord = input("Hier is uw "+hoorntjeOfBakje+" met "+str(bolletjes)+" bolletje(s). Wilt u nog meer bestellen? (Y/N) -> ")
    if antwoord == 'y':
        stap1()
    elif antwoord == 'n':
        print('Bedankt en tot ziens!')
    else:
        print("Sorry, dat snap ik niet...")
        stap3(bolletjes, hoorntjeOfBakje)
stap1()