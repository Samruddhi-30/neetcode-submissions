class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for val in tokens:
            if val=='+':
                stack.append(stack.pop()+stack.pop())
            elif val=='-':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b)-int(a))
            elif val=='*':
                a,b = stack.pop(),stack.pop()
                stack.append(int(a)*int(b))
            elif val=='/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(float(int(b)/int(a))))
            else :
                stack.append(int(val))

        return stack[0]

        