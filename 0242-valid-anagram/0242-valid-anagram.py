class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sm={}
        tm={}
        for c in s:
            if c not in sm:
                sm[c]=1
            else:
                sm[c]+=1
        for c in t:
            if c not in tm:
                tm[c]=1
            else:
                tm[c]+=1
        return sm==tm