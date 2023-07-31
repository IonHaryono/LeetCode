def validMountainArray(arr: list[int]) -> bool:
    if len(arr) < 3:
        return False
    up = True
    if arr[0] >= arr[1]:
        return False

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1] and up:
            up = False
        elif arr[i] >= arr[i-1] and not up:
            return False
        elif arr[i] == arr[i-1]:
            return False
    return not up

print(
    validMountainArray(arr =
[6,7,7,8,6])
)