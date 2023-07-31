def predictPartyVictory(senate: str) -> str:
    senate = list(enumerate((senate)))
    r = []
    d = []
    counter = len(senate)
    for i in range(len(senate)):
        if senate[i][1] == "R":
            r.append(senate[i][0])
        else:
            d.append(senate[i][0])

    while len(r) != 0 and len(d) != 0:
        if d[0] < r[0]: #Dire wins
            del r[0]
            del d[0]
            d.append(counter)
            counter += 1
            
        else:
            if r[0] < d[0]:
                del d[0]
                del r[0]
                r.append(counter)
                counter += 1
    return "Radiant" if len(d) == 0 else "Dire"

    

        

# print(
#     predictPartyVictory(senate = "RD")
# )


print(
    predictPartyVictory(senate = "DDRRRR")
)
