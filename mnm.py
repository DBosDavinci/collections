from random import randrange

kleuren = ["oranje","blauw","groen","bruin"]
zakList = []

def mnmFunctie(hoeveel:int):
    global zakList
    for x in range(1,(hoeveel+1)):
        zakList.append(kleuren[randrange(0,3)])
        x+=1
    print(zakList)

hoeveel = int(input("Hoeveel kleuren moeten er aan de zak m&m's toegevoegd worden?"))
mnmFunctie(hoeveel)