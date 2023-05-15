def romanToInt(s):
    romanList = []
    for i in s:
        romanList.append(i)
    print(romanList)

    romanDict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }   

    #convert into numbers
    romanValueList = []
    for i in range(len(romanList)):
        romanValueList.append(romanDict[s[i]])
    print(romanValueList)
     



    #checking if smaller number is before a bigger number
    romanCalcValueList = []
    for i in range(len(romanValueList)):
        skipState = False
        while i < len(romanValueList) - 1:
            if romanValueList[i] < romanValueList[i+1]:
                maths = int(romanValueList[i+1]) - int(romanValueList[i])
                romanCalcValueList.append(maths)
                del romanValueList[i+1]
                skipState = True
                break
            else:
                romanCalcValueList.append(romanValueList[i])
                break

        if skipState == False and i == len(romanValueList) - 1:
            romanCalcValueList.append(romanValueList[-1])
    #adding the numbers
    totalNumber = 0
    for i in range(len(romanCalcValueList)):
        totalNumber += int(romanCalcValueList[i])
    
    
    
    
    print(romanCalcValueList)

    return totalNumber

# print(romanToInt("MCMXCIV"))
# print(romanToInt("LVIII"))
print(romanToInt("LIV"))
print(romanToInt("MDCCCLXXXIV"))
