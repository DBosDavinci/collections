from random import randrange

kleuren = ["oranje","blauw","groen","bruin"]

def mnmFunctieList(hoeveel:int):
    zakList = []
    for x in range(1,(hoeveel+1)):
        zakList.append(kleuren[randrange(0,4)])
        x+=1
    print(zakList)

def mnmFunctieDict(hoeveel:int):
    zakDictionary = {"oranje":0,"blauw":0,"groen":0,"bruin":0}
    for x in range(1,(hoeveel+1)):
        kleur = kleuren[randrange(0,4)]
        zakDictionary[kleur] = zakDictionary[kleur] + 1
        x+=1
    print(zakDictionary)

hoeveel = int(input("Hoeveel kleuren moeten er aan de zak m&m's toegevoegd worden?"))
mnmFunctieList(hoeveel)
mnmFunctieDict(hoeveel)