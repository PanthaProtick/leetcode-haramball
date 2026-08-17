class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        size=len(triangle)
        dp=[]

        for i in range(size):
            arr=[]
            for j in range(i+1):
                arr.append(99999999)
            dp.append(arr)

        dp[0][0]=triangle[0][0]
        for i in range(1,size):
            for j,item in enumerate(triangle[i]):
                ans=99999999
                if j-1>=0:
                    ans=min(ans,dp[i-1][j-1])
                if j<len(triangle[i-1]):
                    ans=min(ans,dp[i-1][j])
                dp[i][j]=ans+item

        return min(dp[-1])