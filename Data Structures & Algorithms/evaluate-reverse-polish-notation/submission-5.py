class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i!="+" and i!="-" and i!="*" and i!="/":
                stack.append(i)
                continue
            
            a = int(stack.pop())
            b = int(stack.pop())
            
            if i=="+":
                stack.append(a+b)
            elif i=="-":
                stack.append(b-a)
            elif i=="*":
                stack.append(a*b)
            elif i=="/":
                stack.append(b/a)
        
        return int(stack[-1])



