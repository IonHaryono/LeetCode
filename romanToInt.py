def romanToInt(s):
    romanList = []
    for i in s:
        romanList.append(i)
    print(romanList)
        
    romanLetters = ["I","V","X","L","C","D","M"]
    romanValues = ["1","5","10","50","100","500","1000"]
    
    #convert into numbers
    romanValueList = []
    for i in range(len(romanList)):
        for j in range(len(romanLetters)):
            if str(romanList[i]) == str(romanLetters[j]):
                romanValueList.append(int(romanValues[j]))
                
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
