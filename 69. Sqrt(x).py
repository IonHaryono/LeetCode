def mySqrt(x: int) -> int:
    i = 1
    while i * i <= x:
        i += 1
    return i - 1
        


print(
    mySqrt(x = 4)
)