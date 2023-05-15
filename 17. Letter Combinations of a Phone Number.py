def letterCombinations(digits: str) -> list[str]:
    digitLetters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }    
    store = []
    for i in range(len(digits)):
        store.append(digitLetters[digits[i]])
    print("store: ", store)
    
    def combinations(list1, list2):
        finalList = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                finalList.append(list1[i] + list2[j])
        
        # aa = ""
        # for i in range(len(finalList)):
        #     aa += str(finalList[i])
        # return aa
        print("finalList: " + str(finalList))
        return finalList

    #0
    final = []
    if len(digits) == 0:
        return []
    #1
    elif len(digits) == 1:
        for i in range(len(store[0])):
            final.append(store[0][i])

    #2
    elif len(digits) == 2:
        return combinations(store[0], store[1])

    #3
    elif len(digits) >= 3:
        combSet = store[0]
        for i in range(1, len(digits)):
            combSet = combinations(combSet, store[i])
        final = combSet

    # storeCombinations = combinations(store[0], store[1])
    # print("storeCombinations: " + str(storeCombinations))
    
    
    
    # finalFinal = []
    # for i in range(len(final)):
    #     for j in range(len(final[i])):
    #         finalFinal.append(final[i][j])

    return final




print(letterCombinations("2234"))
# print(letterCombinations("23"))