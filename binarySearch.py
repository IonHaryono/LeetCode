def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l



print(
    binarySearch(
        nums =  [0,1,2,3,7,9,9,9,9,55,66],
        target = 9
        )
    )