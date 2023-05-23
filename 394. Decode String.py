def decodeString(s: str) -> str:
    # output = ""
    def expander(s1, numberLength):
        # print(s1)
        # print(numberLength)
        # print(s1[numberLength:])
        # print(int(s1[:numberLength - 1]))
        return s1[numberLength:] * int(s1[:numberLength - 1])
    
    openBracketsList = []

    for i in range(len(s)):
        if s[i] == "[":
            openBracketsList.append(i)
        elif s[i] == "]":
            numberLength = 1
            while openBracketsList[-1] - numberLength >= 0 and s[openBracketsList[-1] - numberLength].isnumeric():
                numberLength += 1
            expanderHold = expander(s[openBracketsList[-1] - numberLength + 1:i], numberLength) #includes the number
            # print(s[:openBracketsList[-1] - numberLength + 1])
            # print(expanderHold)
            # print(s[i + 1:])
            s = s[:openBracketsList[-1] - numberLength + 1] + expanderHold + s[i + 1:]
            # print(s)
            break

    for i in s:
        if i == "[":
            s = decodeString(s)
            break
    return s



    # if "[" in s:
    #     decodeString(s)
    # else:
    #     return s

# print(
#     decodeString(s = "3[a]2[bc]")
# )


print(
    decodeString(s = "10[a2[c]]")
)

# print(
#     decodeString("2[abc]3[cd]ef")
# )
