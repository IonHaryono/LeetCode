def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()

    i = 0
    k = len(nums)-1
    j = 1
    print(nums)
    previousSum = sum(nums[i], nums[j], nums[k])

    def sum(n1, n2, n3):
        return n1 + n2 + n3

    while i < k:
        while j < k:
            if sum(nums[i], nums[k-1], nums[k]) < previousSum:
                






print(
    threeSumClosest(nums = [-1,2,1,-4], target = 1)
)