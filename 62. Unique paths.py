def uniquePaths(m: int, n: int) -> int:

    memo = [[0 for _ in range(n)] for _ in range(m)]
    #m = rows
    #n = columns

    #initialisation:
    for i in range(n):
        memo[0][i] = 1
    for j in range(m):
        memo[j][0] = 1


    for columns in range(1, m):
        for rows in range(1, n):
            memo[columns][rows] = memo[columns - 1][rows] + memo[columns][rows - 1]
    print(memo)
    return memo[-1][-1]






print(uniquePaths(m = 3, n = 7))