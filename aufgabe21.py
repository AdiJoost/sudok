def concatLists(list1, list2):
    list3 = []
    for i in range (len(list1)):
        list3.append(list1[i])
    for i in range(len(list2)):
        list3.append(list2[i])
    return list3

liste1 = [1,2,3,4]
liste2 = [7,6,8]
liste3 = concatLists(liste1, liste2)
print(liste3)