listeA = [1,3,11,23,4,5]
listeB = [4,3,11,23,7,8]

#Teilaufgabe A
def isIdentical(listeA, listeB) -> bool:
    if (len(listeA) != len(listeB)):
        return False
    for i in range(len(listeA)):
        if (listeA[i] != listeB[i]):
            return False
    return True

print(f"Are lists identical? {isIdentical(listeA, listeB)}")

#Teilaufgabe B
def whereEqual(listeA, listeB) -> list:
    if (len(listeA) != len(listeB)):
        return None
    listeBool = []
    for i in range(len(listeA)):
        if (listeA[i] == listeB[i]):
            listeBool.append(True)
        else:
            listeBool.append(False)
    return listeBool

listeBool = whereEqual(listeA, listeB)
print(f"\nWhere are they equal?\n{listeBool}")

#Teilaufgabe C
def areEqualLenght(listeA, listeB) -> bool:
    if (len(listeA) == len(listeB)):
        return True
    return False

print(f"\nAre lists equal length? {areEqualLenght(listeA, listeB)}")

#Teilaufgabe D
def sortList(myList) -> list:
    sorted = []
    myListCopy = myList.copy()
    while len(myListCopy) > 0:
        sorted.append(min(myListCopy))
        myListCopy.remove(min(myListCopy))
    return sorted

listC = []
listC.extend(listeA)
listC.extend(listeB)

sortedList = sortList(listC)
print(f"\nThe list sorted:\n{sortedList}")
