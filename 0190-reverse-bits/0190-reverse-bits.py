class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        for i in range(32):
            if n & 1 == 1:
                ans+=(2**(31-i))
            n=n>>1
        return ans