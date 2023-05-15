def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    if len(nums) == 1:
        return False
    
    i = 0
    j = 1
    while i < len(nums):
        while j < len(nums):
            if nums[i] == nums[j]:
                if abs(j-i) <= k:
                    return True
                else:
                    j += 1
            else:
                j += 1
        i += 1
        j = i + 1
    return False


print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))