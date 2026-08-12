class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[-2 for i in range(amount+1)]
        def func(total):
            if total<0:
                return -1
            elif total==0:
                return 0
            else:
                if dp[total]!=-2:
                    return dp[total]
                ans=2**31-1
                for coin in coins:
                    val=func(total-coin)
                    if val!=-1:
                        ans=min(1+val,ans)
                if ans==2**31-1:
                    dp[total]=-1
                    return dp[total]
                else:
                    dp[total]=ans
                    return dp[total]

        return func(amount)