class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        ans=left
        while left<=right:
            mid=left+(right-left)/2
            sqr=mid*mid
            if sqr==x:
                return mid
            elif sqr<x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans