from random import randint

def getUserInput():
    foundInt = False
    while not foundInt:
        userInput = input("Geben Sie einen Integer ein:")
        try:
            returnInt = int(userInput)
            foundInt = True
        except ValueError:
            print("It should be an Integer")
    return returnInt

#Aus Aufgabe 23 übernommen
def sortList(myList) -> list:
    sorted = []
    myListCopy = myList.copy()
    while len(myListCopy) > 0:
        sorted.append(min(myListCopy))
        myListCopy.remove(min(myListCopy))
    return sorted

userInput = getUserInput()
myList = [randint(1,userInput*10) for i in range(userInput)]
sortedList = sortList(myList)
print(f"Your generated List:\n {sortedList}")
