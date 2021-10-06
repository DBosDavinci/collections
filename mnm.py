from random import randrange

kleuren = ["oranje","blauw","groen","bruin"]
zakList = []
zakDictionary = {"oranje":0,"blauw":0,"groen":0,"bruin":0}
hoeveel = int(input("Hoeveel kleuren moeten er aan de zak m&m's toegevoegd worden?"))

def mnmFunctieList(hoeveel:int):
    for x in range(1,(hoeveel+1)):
        zakList.append(kleuren[randrange(0,4)])
    print(zakList)

def mnmFunctieDict(hoeveel:int):
    for x in range(1,(hoeveel+1)):
        kleur = kleuren[randrange(0,4)]
        zakDictionary[kleur] = zakDictionary[kleur] + 1
    print(zakDictionary)

def mnmFunctieSorteer(SorteerList:list,SorteerDict:dict):
    global hoeveel
    o = SorteerDict.get("oranje")
    bl = SorteerDict.get("blauw")
    g = SorteerDict.get("groen")
    br = SorteerDict.get("bruin")
    for x in range(0,hoeveel):
        if SorteerList[x] == "oranje":
            o = o + 1
        elif SorteerList[x] == "blauw":
            bl = bl + 1
        elif SorteerList[x] == "groen":
            g = g + 1
        elif SorteerList[x] == "bruin":
            br = br + 1
    print("Er zijn {} oranje, {} blauwe, {} groene en {} bruine m&m's".format(o,bl,g,br))

mnmFunctieList(hoeveel)
mnmFunctieDict(hoeveel)
mnmFunctieSorteer(zakList,zakDictionary)