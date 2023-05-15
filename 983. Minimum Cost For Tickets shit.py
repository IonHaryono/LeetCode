def mincostTickets(days: list[int], costs: list[int]) -> int:
    def costCalculation(daysForCalc):
        print("daysForCalc:", daysForCalc)
        price = 0
        if daysForCalc > 28:
            price += costs[2]

        elif 6 < daysForCalc < 29:
            price += (daysForCalc // 7) *costs[1]
            daysForCalc = daysForCalc % 7
            if daysForCalc > 0:
                price += daysForCalc * costs[0]
            if price > costs[2]:
                return costs[2]


        elif daysForCalc < 7:
            price += daysForCalc * costs[0]
        print("price:", price)
        return price

    diffList = []
    dayHolder = 0
    totalCost = 0


    for idx in range(len(days)):
        if days[idx] - dayHolder > 30:
            diffList.append(days[idx]-(dayHolder + 30))
        else:
            diffList.append(days[idx] - dayHolder)
        print(diffList)

    for i in range(1,len(diffList)):
        if diffList[i] < diffList[i - 1]:
            totalCost += costCalculation(diffList[i-1])

    totalCost += costCalculation(diffList[i])

    return totalCost




# print(mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30], costs = [2,7,15]))
print(mincostTickets(days = [1,4,6,7,8,20,40, 69, 100] costs = [2,7,15]))
print(mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))

