def addDigits(num: int) -> int:
    while num > 9:
        holder = 0
        for i in range(len(str(num))):
            holder = int(str(num)[i])
        num = holder
    return num

print(
    addDigits(num = 38)
)