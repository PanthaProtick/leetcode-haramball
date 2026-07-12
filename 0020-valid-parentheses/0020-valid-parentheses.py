from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening=set(['(','{','['])
        closing=set([')','}',']'])
        stack=deque()

        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if stack:
                    char=stack.pop()
                else:
                    return False
                if (c==')' and char!='(') or (c=='}' and char!='{') or (c==']' and char!='['):
                    return False
        if len(stack)==0:
            return True
        else:
            return False