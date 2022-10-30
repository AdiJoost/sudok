
def reverseList(myList):
    reversed = []
    for i in range(1, len(myList) + 1):
        reversed.append(myList[-i])
    return reversed

myList = [1,2,3,4,5,6,7,8,9]
listeReversed = reverseList(myList)
print(listeReversed)