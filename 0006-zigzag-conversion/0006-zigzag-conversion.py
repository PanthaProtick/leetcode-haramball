class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        rows=[]
        for i in range(numRows):
            rows.append("")
        size=len(s)
        down=True
        k=-1
        for i in range(size):
            l=s[i]
            if down:
                if k<numRows-1:
                    k+=1
                    rows[k]+=l
                else:
                    down=False
                    k=numRows-2
                    rows[k]+=l
            else:
                if k>0:
                    k-=1
                    rows[k]+=l
                else:
                    down=True
                    k=1
                    rows[k]+=l
        ans=""
        for row in rows:
            ans+=row
        return ans
            