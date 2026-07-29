class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans=[]

        def backtrack(start, comb):
            if len(comb)==k:
                ans.append(list(comb))
                return

            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()

        backtrack(1,[])
        return ans