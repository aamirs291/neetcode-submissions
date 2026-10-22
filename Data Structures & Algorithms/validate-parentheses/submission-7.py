class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
                continue

            if not stack:
                return False
            
            else:
                if stack[-1]=="(" and char==")":
                    stack.pop()

                elif stack[-1]=="[" and char=="]":
                    stack.pop()

                elif stack[-1]=="{" and char=="}":
                    stack.pop()
                
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
                
