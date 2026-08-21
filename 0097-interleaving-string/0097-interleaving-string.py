class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        size1=len(s1)
        size2=len(s2)
        size3=len(s3)

        if size1+size2!=size3:
            return False

        dp={}

        def func(i,j):
            if i==size1 and j==size2:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            
            k=i+j
            ans=False

            if i<size1 and s1[i]==s3[k]:
                ans=ans or func(i+1,j)
            if j<size2 and s2[j]==s3[k]:
                ans=ans or func(i,j+1)
            
            dp[(i,j)]=ans
            return ans
        
        return func(0,0)