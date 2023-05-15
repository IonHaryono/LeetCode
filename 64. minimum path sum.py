from ctypes import memmove


def minPathSum(grid: list[list[int]]) -> int:
    m = len(grid) #columns
    n = len(grid[0]) #rows 
    
    memo = [[0 for _ in range(n)] for _ in range(m)]

    #initialise
    memo[0][0] = grid[0][0]
    for i in range(1, m):
        memo[i][0] = memo[i-1][0] + grid[i][0]
    for i in range(1, n):
        memo[0][i] = memo[0][i-1] + grid[0][i]
    # print(memo)


    for column in range(1, m):
        for row in range(1, n):
            memo[column][row] = min(memo[column - 1][row], memo[column][row - 1]) + grid[column][row]

    return memo[-1][-1]


# print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))
