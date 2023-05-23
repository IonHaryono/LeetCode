def stoneGame(piles: list[int]):
    #True if Alice wins
    #False if Bob wins
    memo = [0 for i in range(len(piles) + 2)]
    print(memo)

    #Alice goes first = odd
    #Bobs goes second = even

    if len(piles) <= 2:
        return True


    i = 2
    while memo[-1] == 0:
        if len(piles) == 1:
            memo[i] = piles[0] + memo[i - 2]

        elif piles[0] - piles[1] > piles[-1] - piles[-2]:
            memo[i] = piles[0] + memo[i - 2]
            del piles[0]
        elif piles[0] - piles[1] < piles[-1] - piles[-2]:
            memo[i] = piles[-1] + memo[i - 2]
            del piles[-1]
        else:
            if piles[0] > piles[-1]:
                memo[i] = piles[0] + memo[i - 2]
                del piles[0]
            else:
                memo[i] = piles[-1] + memo[i - 2]
                del piles[-1]
        i += 1

    print(memo)

    return memo[-2] > memo[-1]


# print(
#     stoneGame(piles = [5,3,4,5])
# )

# print(
#     stoneGame(piles = [8,9,7,6,7,6])
# )
print(
    stoneGame(piles = [6,3,9,9,3,8,8,7])
)