def isValid(s: str) -> bool:
    st = []
    d = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    for i in range(len(s)):
        if s[i] in d:
            st.append(s[i])                
        elif len(st) == 0 and s[i] not in d:
            return False
        elif d[st[-1]] == s[i]:
            st.pop()
        else:
            return False
    return True if len(st) == 0 else False

print(
    isValid(s = "(])")
)