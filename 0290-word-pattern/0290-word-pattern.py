class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        m={}
        s=s.split()
        if len(pattern)!=len(s):
            return False
        size=len(pattern)
        for i in range(size):
            w=s[i]
            c=pattern[i]
            if c not in m:
                if w in m.values():
                    return False
                else:
                    m[c]=w
            elif m[c]!=w:
                return False
        return True