class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1

        while i>=0:
            digits[i]+=1
            if digits[i]<10:
                return digits
            digits[i]-=10
            if i==0:
                digits.insert(0,1)
            i-=1
        
        return digits