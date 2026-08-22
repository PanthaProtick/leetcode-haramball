class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1=len(word1)
        size2=len(word2)
        dp=[]

        for i in range(size1+1):
            dp.append([0 for j in range(size2+1)])

        x=size1
        for i in range(size1+1):
            dp[i][size2]=x
            x-=1

        y=size2
        for j in range(size2+1):
            dp[size1][j]=y
            y-=1

        for i in range(size1-1,-1,-1):
            for j in range(size2-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])+1

        return dp[0][0]