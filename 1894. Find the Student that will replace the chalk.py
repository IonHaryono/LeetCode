def chalkReplacer(chalk: list[int], k: int) -> int:
    totalChalk = sum(chalk)
    remainder = k % totalChalk
    for i in range(len(chalk)):
        print("Remainder:", remainder)
        if remainder >= chalk[i]:
            remainder -= chalk[i]
        elif remainder < chalk[i]:
            return i
        else:
            print("Error")
    




print(chalkReplacer(chalk = [5,1,5], k = 22))
print(chalkReplacer(chalk = [3,4,1,2], k = 25))