class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        
        else:
            def rle(s):
                size=len(s)
                ans=""
                c=s[0]
                cnt=1

                for i in range(1,size):
                    if c==s[i]:
                        cnt+=1
                    else:
                        ans+=(str(cnt)+c)
                        c=s[i]
                        cnt=1

                ans+=(str(cnt)+c)
                return ans
                    
            return rle(self.countAndSay(n-1))