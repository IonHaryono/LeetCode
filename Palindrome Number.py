def isPalindrome(x):
    correctOrderList = []
    otherOtherList = []
    x = str(x)
    for i in range(len(x)):
        correctOrderList.append(x[i])
        otherOtherList.append(x[-1-i])

    print(correctOrderList)
    print(otherOtherList)



# print(isPalindrome(123))
isPalindrome(1256) 