class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        if len(s)<2:
            return False

        for i in range(len(s)):
            if s[i]!=")" and s[i]!="]" and s[i]!="}":
                stack.append(s[i])
            elif not stack:
                return False
            else:
                if s[i]==")" and stack[-1]=="(":
                    stack.pop()
                elif s[i]=="]" and stack[-1]=="[":
                    stack.pop()
                elif s[i]=="}" and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
        print(stack)
        return True if not stack else False
        