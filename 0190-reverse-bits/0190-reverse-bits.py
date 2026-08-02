class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        for i in range(32):
            if (n >> i) & 1 == 1:
                ans+=(2**(31-i))
        return ans