class Solution(object):
    m={
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(j):
            if j>=len(digits):
                return []
            digit=digits[j]
            string=dfs(j+1)
            ans=[]
            for char in self.m[digit]:
                if string:
                    ans.extend([char+s for s in string])
                else:
                    ans.extend([char])
            return ans
        if digits:
            return dfs(0)
        else:
            return []

                