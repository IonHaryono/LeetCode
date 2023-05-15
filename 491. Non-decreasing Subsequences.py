def findSubsequences(nums: list[int]) -> list[list[int]]:
    output = []
    for firstNumber in range(len(nums)):
        listHolder = []
        listHolder.append(nums[firstNumber])
        for pointer in range(1, len(nums)):
            if nums[pointer] >= firstNumber:
                listHolder.append(nums[pointer])
                output.append(listHolder)
        
    return output

print(findSubsequences(nums = [4,6,7,7]))