def countRectangles(rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
    
    output = []

    def pointChecker(point):
        print("point:", point)
        tally = 0
        pointX, pointY = point[0], point[1]
        for rectangle in rectangles:

            print("rectangle:", rectangle)
            print("tally:", tally)
            if rectangle[0] >= pointX and rectangle[1] >= pointY:
                tally += 1 
        return tally        

    for i in range(len(points)):
        output.append(pointChecker(points[i]))

    return output
print(countRectangles(rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]))
print(countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]))