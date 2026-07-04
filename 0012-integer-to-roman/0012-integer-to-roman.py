class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        conv={
            "1":"I",
            "5":"V",
            "10":"X",
            "50":"L",
            "100":"C",
            "500":"D",
            "1000":"M",
        }

        factor=1
        ans=""
        while num>0:
            digit=num%10
            num/=10
            if digit==0:
                factor*=10
                continue
            if digit<=3:
                ans+=(conv[str(factor)]*digit)
            elif digit==4:
                ans+=(conv[str(factor*5)]+conv[str(factor)])
            elif digit<9:
                ans+=(conv[str(factor)]*(digit-5)+conv[str(factor*5)])
            elif digit==9:
                ans+=(conv[str(factor*10)]+conv[str(factor)])
            factor*=10
        ans=ans[::-1]
        return ans
        