class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        factor=5
        while True:
            x=n//factor
            if x==0:
                break
            ans+=x
            factor*=5
        return ans