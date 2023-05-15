def mergeTwoLists(list1, list2):
    if len(list2) == 0:
        return list1
    
    finalList = []
    firstListi = 0
    secondListj = 0
    while firstListi < len(list1):
        while secondListj < len(list2):
            if list1[firstListi] == list2[secondListj]:
                list2.insert(secondListj, list1[firstListi])
                break
            elif list1[firstListi] < list2[secondListj]:
                list2.insert(secondListj, list1[firstListi])
                break
            elif list1[firstListi] > list2[secondListj]:
                secondListj += 1

        secondListj = 0
        firstListi += 1

    return list2


print(mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))
print(mergeTwoLists(list1 = [], list2 = []))
print(mergeTwoLists(list1 = [], list2 = [1]))
print(mergeTwoLists(list1 = [1], list2 = []))