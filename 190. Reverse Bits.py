def reverseBits(n: int) -> int:
    output = 0
    for i in range(31, -1, -1):
        output = output|((n&1)<<i)
        n = n>>1
    return output

print(
    reverseBits(n = 11111111111111111111111111111101)
    )