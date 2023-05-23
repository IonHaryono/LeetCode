def lengthOfLongestSubstring(s: str) -> int:
    sSet = set()
    r, l = 0, 0
    output = 0
    while r < len(s):
        while s[r] in sSet:
            sSet.remove(s[l])
            l += 1
        sSet.add(s[r])
        output = max(output, len(sSet))
        r += 1
    return output




print(
lengthOfLongestSubstring(s = "abcabcbb")
)