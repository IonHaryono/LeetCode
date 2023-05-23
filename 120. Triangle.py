def minimumTotal(triangle: list[list[int]]) -> int:
    minSum = triangle[0][0]

    if len(triangle) <= 1:
        return minSum
    
    for depth in range(1, len(triangle)):
        #Left
        triangle[depth][0] += triangle[depth - 1][0]

        #Middle
        for i in range(1, len(triangle[depth])-1):
            triangle[depth][i] += min(triangle[depth - 1][i - 1], triangle[depth - 1][i])

        #Right
        triangle[depth][-1] += triangle[depth - 1][-1]

    return min(triangle[-1])

print(
    minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]])
)