from collections import deque
class Solution(object):
    def is_number(self, value:float)->bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens:List[str])->int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=deque()
        operators={'+','-','*','/'}
        for token in tokens:
            if token in operators:
                a=stack.pop()
                b=stack.pop()
                if token=='+':
                    stack.append(b+a)
                elif token=='-':
                    stack.append(b-a)
                elif token=='*':
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
            elif self.is_number(token):
                stack.append(int(token))
        if stack:
            return stack.pop()
        else:
            return 0    