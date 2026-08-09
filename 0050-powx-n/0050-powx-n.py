class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def func(base,exp):
            if exp==0:
                return 1
            elif exp%2==0:
                return func(base*base,exp//2)
            else:
                return base*func(base*base,((exp-1)//2))
        ans=func(x,abs(n))
        if n>=0:
            return float(ans)
        else:
            return 1/ans