def spiralOrder(matrix: list[list[int]]) -> list[int]:
    maxHorizontal = len(matrix[0])
    maxVertical = len(matrix)
    horiCounter = 0
    vertCounter = 0


    numberCounter = 0
    spiralArray = [0 for _ in range(maxVertical * maxHorizontal)]
    print(spiralArray)


    while numberCounter <= maxHorizontal * maxVertical:
        #LR
        for i in range(maxHorizontal - vertCounter * 2):
            spiralArray[numberCounter] = matrix[horiCounter][vertCounter + i]
            numberCounter += 1
        

        for j in range(1, maxVertical - 2 * horiCounter):
            spiralArray[numberCounter] = matrix[horiCounter + j][maxVertical - vertCounter]
            numberCounter += 1

        for k in range((maxHorizontal - 1) - (2 * vertCounter)):
            spiralArray[numberCounter] = matrix[maxVertical - 1 - horiCounter][maxHorizontal - 2 - vertCounter - k]
            numberCounter += 1

        for l in range((maxVertical - 1) - (2 * horiCounter)):
            spiralArray[numberCounter] = matrix[maxVertical - 2 - horiCounter - l][maxHorizontal - 1 - vertCounter]
            numberCounter += 1
            
        numberCounter += 1
        horiCounter += 1
        vertCounter += 1


    return spiralArray






print(
    spiralOrder(matrix =  [[1,2,3,4],[5,6,7,8],[9,10,11,12]])
)