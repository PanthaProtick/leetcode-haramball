class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]

        def backtrack(number,closed,path):
            if number==0:
                for i in range(closed):
                    path+=')'
                ans.append(str(path))
                path=path[:-closed]
                return

            if number<closed:
                path+=')'
                backtrack(number,closed-1,path)
                path=path[:-1]
            path+='('
            backtrack(number-1,closed,path)
            path=path[:-1]

        backtrack(n,n,'')
        return ans   