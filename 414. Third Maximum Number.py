def thirdMax(nums: list[int]) -> int:
    if len(nums) < 3:
        return max(nums)
    
    
    nums.sort()
    uniqueNums = set()
    counter = 1
    for i in range(len(nums)):
        if nums[-1 - i] not in uniqueNums:
            if counter == 3:
                return nums[-1 -i]
            elif counter <= 2 and nums[-1 - i] == nums[0]:
                return max(nums)
            uniqueNums.add(nums[-1 -i])
            counter += 1
            

print(
    thirdMax(nums =[1,1,2])
)