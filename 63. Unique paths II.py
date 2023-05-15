def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    memo = [[0 for _ in range(n)] for _ in range(m)]
    #m = rows
    #n = columns

    #initialisation:
    # for i in range(n):
    #     if obstacleGrid[0][i] != 1:
    #         memo[0][i] = 1
    # for j in range(m):
    #     if obstacleGrid[j][0] != 1:
    #         memo[j][0] = 1

            
    # if m == 1 or n == 1:
    #     if m == 1:
    #         if max(obstacleGrid[0]) == 1:
    #             return 0
    #     for i in range(m):
    #         if obstacleGrid[i][0] == 1:
    #             return 0
    #     return 1



    for columns in range(m):
        for rows in range(n):
            if obstacleGrid[columns][rows] == 1:
                memo[columns][rows] = 0
            elif columns == rows == 0:
                memo[columns][rows] = 1
            else:
                memo[columns][rows] = memo[columns - 1][rows] + memo[columns][rows - 1]
            print(memo)

    return memo[-1][-1]


# print((uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))) 
print((uniquePathsWithObstacles(
[[0,0,1,0]]))) 