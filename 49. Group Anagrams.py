def groupAnagrams(strs: list[str]) -> list[list[str]]:
    l = []
    output = []
    for i in range(len(strs)): #i iterates through strs
        d = {}
        for j in range(len(strs[i])): #j interates through letters of strs
            if strs[i][j] not in d:
                d[strs[i][j]] = 1
            else:
                d[strs[i][j]] += 1
        output.append([])
        if d not in l:
            l.append(d)
        for k in range(len(l)): #k iterates through list of dicts (l)
            if l[k] == d:
                output[k].append(strs[i])
    while [] in output:
        output.remove([])
    return output

print(
    groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
)

