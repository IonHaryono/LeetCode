def isAnagram(s: str, t: str) -> bool:
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    
    for j in range(len(t)):
        if t[j] in d:
            if d[t[j]] > 1:
                d[t[j]] -= 1
            else:
                del d[t[j]]
        else:
            return False

    return True if len(d) == 0 else False

print(
    isAnagram(s ="anagram", t ="nagaram")
)