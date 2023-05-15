def PredictTheWinner(nums: list[int]) -> bool:
    
    player1memo = [0 for _ in range(len(nums) // 2 + 2)]
    player2memo = [0 for _ in range(len(nums) // 2 + 1)]    
    print(player1memo)
    print(player2memo)
    
    
    
    goLeft = False
    leftPointer = 0
    rightPointer = len(nums) - 1
    i = 1
    j = 1
    player1Turn = True
    skip = False

    if len(nums) == 1:
        return True


    print(nums)
    while leftPointer <= rightPointer:

#first player
        if i < len(player1memo) and player1Turn:
            if len(nums[leftPointer:rightPointer + 1]) == 1:
                player1memo[i] = player1memo[i - 1] + nums[rightPointer] 
                leftPointer += 1
                rightPointer -= 1
                skip = True




            elif nums[leftPointer] - nums[leftPointer + 1] > nums[rightPointer] - nums [rightPointer - 1]:
                goLeft = True
            else:
                goLeft = False


            if goLeft == True and not skip: 
                player1memo[i] = player1memo[i - 1] + nums[leftPointer]
                leftPointer += 1
                skip = False
            elif goLeft == False and not skip:
                player1memo[i] = player1memo[i - 1] + nums[rightPointer] 
                rightPointer -= 1
                skip = False
            i += 1
            print("player1memo: ", player1memo)
            print(nums[leftPointer:rightPointer + 1])
            player1Turn = False
            


#second player
        if j < len(player2memo) and not player1Turn:
            if len(nums[leftPointer:rightPointer + 1]) == 1:
                player2memo[j] = player2memo[j - 1] + nums[rightPointer] 
                leftPointer += 1
                rightPointer -= 1
                skip = True



            elif nums[leftPointer] - nums[leftPointer + 1] > nums[rightPointer] - nums [rightPointer - 1]:
                goLeft = True
            else:
                goLeft = False
            
            if goLeft == True and not skip:
                player2memo[j] = player1memo[j - 1] + nums[leftPointer]
                leftPointer += 1
                
            elif goLeft == False and not skip:
                player2memo[j] = player2memo[j - 1] + nums[rightPointer] 
                rightPointer -= 1
            skip = False
            j += 1
            print("player2memo: ", player2memo)
            print(nums[leftPointer:rightPointer + 1])
            player1Turn = True

        


    return max(player1memo) >= max(player2memo)


# print(PredictTheWinner(nums = [1,5,2]))
# print(PredictTheWinner(nums = [1,5,233,7]))
# print(PredictTheWinner(nums = [0]))
# print(PredictTheWinner(nums = [2,4,55,1]))
# print(PredictTheWinner(nums = [1,100,1,2,3,4,5]))
print(PredictTheWinner(nums = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]))
# print(PredictTheWinner(nums = [100,6,5,9,200,7,300,250,220,9,6,200,100,100,4,200,8,7,1]))

# print(PredictTheWinner(nums = [2,4,55,1,323,24,17,9,300,2]))
