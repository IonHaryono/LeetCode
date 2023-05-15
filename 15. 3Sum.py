def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    i = 0
    j = len(nums) - 1
    storeList = []
    output = set()
    d = {}

    while i + 1 < j: 
        k = i + 1
        j = len(nums) - 1
        sum = nums[i] + nums[j]
        
        while k < j:
            if sum <= 0:
                if nums[k] < 0:
                    k += 1
                elif sum + nums[k] > 0: 
                    j -= 1
                    sum = nums[i] + nums[j]
                elif sum + nums[k] == 0:
                    output.add(tuple(sorted([nums[i], nums[k], nums[j]])))
                    k += 1
                else: #Sum < 0 and nums[k] > 0 but sum + nums[k] != 0
                    k +=1 
            elif sum > 0:
                if nums[k] > 0:
                    break
                elif sum + nums[k] > 0:
                    j -=1
                    sum = nums[i] + nums[j]
                elif sum + nums[k] == 0:
                    output.add(tuple(sorted([nums[i], nums[k], nums[j]])))
                    k += 1
                else: #sum > 0, nums[k] < 0
                    k += 1
        i += 1
    return list(output)
        

# print(threeSum(nums = [-1,0,1,2,-1,-4]))
# print(threeSum(nums = [0,1,1]))   
# print(threeSum(nums = [0,0,0]))
# print(threeSum(nums = [-2,0,1,1,2]))
# print(threeSum(nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(threeSum(nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))
#[34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]