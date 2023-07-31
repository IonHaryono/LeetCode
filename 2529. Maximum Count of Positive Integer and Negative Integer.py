def maximumCount(nums: list[int]) -> int:
    def posBinarySearch(l, r, nums, target):
        while l <= r:
            # print("l:",l)
            # print("r:", r)
            mid = (l + r) // 2
            # print("m:", mid)
            # print("nums[m]:", nums[mid])            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        

    def negBinarySearch(l, r, nums, target):
        while l <= r:
            # print("l:",l)
            # print("r:", r)
            mid = (l + r) // 2
            # print("m:", mid)
            # print("nums[m]:", nums[mid])   
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return r


    return(max(len(nums) - posBinarySearch(0, len(nums) -1 , nums, 0), negBinarySearch(0, len(nums) - 1, nums, 0) + 1))

    


# print(
#     maximumCount(nums = [-3,-2,-1,0,0,1,2])
# )

# print(
#     maximumCount(nums = [-1])
# )

print(
    maximumCount(nums = [-2, -2, -1])
)