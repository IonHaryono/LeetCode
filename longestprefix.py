def longestCommonPrefix(strs: list[str]) -> str:
    output = ""
    storeLetter = "" 

    if len(strs) < 2:
        return strs[0]

    counter = 0
    for i in range(len(strs[0])):
        storeLetter = strs[0][i]
        try:
            for k in range(len(strs)):
                if strs[i] == strs[i+k + 1]:
                    counter += 1
        except:
            pass
        if counter == len(strs) - 1:
            return strs[0]


        for j in range(len(strs)):
            try:    
                if strs[1 + j][i] == storeLetter:  
                    # print(strs[1+j][i])
                    if strs[1+j] == strs[-1]:
                        output += storeLetter
                else:
                    return output
            except Exception as e:
                break
                
    return output
            
            
print(longestCommonPrefix(strs = ["cir","car"]))
print(longestCommonPrefix(strs = ["flower","flow","flight","flying"]))
print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ["flower","fower","flower"]))
print(longestCommonPrefix(strs = ["flower","flower","flower"]))

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        if (len(strs) == 0):
            return ""

        for i in range(len(strs[0])):

            storedChar = strs[0][i]

            for j in range(len(strs)):
                if (i == len(strs[j]) or strs[j][i] != storedChar):
                    return strs[0][0:i];
        return strs[0]
"""
