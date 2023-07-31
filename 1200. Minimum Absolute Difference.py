def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    s = set(arr)
    output = []
    for i in arr:
        if i > 0 and (-i + 1) in s:
            output.append([i])



print(
    minimumAbsDifference([4,2,1,3])
)