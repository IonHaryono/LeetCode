def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    holdList = []
    holdListSum = 0
    res = []
    i = 0
    toContinue = True

    while toContinue:
        while i < len(candidates):
            # print(target)
            # print(candidates[i])

            #add multiples of number
            if target % candidates[i] == 0:
                for _ in range(int(target/candidates[i])):
                    holdList.append(candidates[i])
                print(holdList)
                res.append(holdList)

            
            i += 1


        i = 0


    return res

print(combinationSum(candidates = [2,3,6,7], target = 8))
