from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=deque()
        path=path.split('/')
        home=True
        for d in path:
            if d and d!='.' and d!='..':
                stack.append(d)
                if home:
                    home=False
            elif d=='..':
                if not home:
                    stack.pop()
                    if not stack:
                        home=True
        arr=[]
        while stack:
            arr.append(stack.popleft())
        ans="/"
        for item in arr:
            ans+=(item+'/')
        if len(ans)!=1:
            ans=ans[:-1]
        return ans