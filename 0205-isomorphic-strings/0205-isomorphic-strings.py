class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m={}
        size=len(s)
        for i in range(size):
            sc=s[i]
            tc=t[i]
            if sc not in m:
                if tc not in m.values():
                    m[sc]=tc
                else:
                    return False
            elif m[sc]!=tc:
                return False
        return True