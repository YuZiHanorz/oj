class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for op in tokens:
            if op == '+' or op == '-' or op == '/' or op == '*':
                rt = stack.pop(-1)
                lt = stack.pop(-1)
                if op == '+':
                    stack.append(lt + rt)
                elif op == '-':
                    stack.append(lt - rt)
                elif op == '*':
                    stack.append(lt * rt)
                else:
                    res = lt // rt
                    rest = lt % rt
                    if res < 0 and rest != 0:
                        res += 1
                    stack.append(res)
            else:
                stack.append(int(op))
        return stack[0]
                
                
            
            
