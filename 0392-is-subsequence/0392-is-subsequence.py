class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        sizet=len(t)
        sizes=len(s)
        if sizes==0:
            return True
        for j in range(sizet):
            if s[i]==t[j]:
                i+=1
                if i==sizes:
                    return True
        return False