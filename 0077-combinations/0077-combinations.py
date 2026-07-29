class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(j):
            if j<=0:
                return [[]]

            arr=dfs(j-1)
            ans=[]
            for entry in arr:
                start=entry[-1]+1 if entry else 1

                for i in range(start, n+1):
                    ans.append(entry+[i])
            return ans
        return dfs(k)