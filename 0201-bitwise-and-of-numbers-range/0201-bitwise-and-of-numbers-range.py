class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        temp=1
        for i in range(32):
            if temp>left and temp<=right:
                return 0
            if temp>left and temp>right:
                break
            temp<<=1

        ans=-1

        diff=right-left
        count=0
        for i in range(32):
            if diff&1:
                count=i+1
            diff>>=1

        ans<<=count   
        return ans&left&right