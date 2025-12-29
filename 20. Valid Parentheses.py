class Solution:
    def isValid(self, s: str) -> bool:
        
        open_p = ("{", "[", "(")
        closed_p = ("}", "]", ")")

        stack = []

        for ch in s:
            if ch in open_p:
                stack.append(ch)
            
            elif ch in closed_p:
                if not stack: # if stack is empty, there does not exist a valid open parenthesis for this closed parenthesis.
                    return False
                
                valid_open = open_p[closed_p.index(ch)]
                if stack[-1] != valid_open: # check if most recent open parenthesis in stack is a valid opener for this closing parenthesis
                    return False
                
                stack.pop() # assume that the most recent open parenthesis is valid with this closing parenthesis and we can pop the open parenthesis from the stack


        return len(stack) == 0




