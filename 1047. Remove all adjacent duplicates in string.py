def removeDuplicates(s: str) -> str:
    stack = []
    for i in range(len(s)):
        if len(stack) > 1 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        
    return stack
    
        

print(removeDuplicates(s = "abbaca"))