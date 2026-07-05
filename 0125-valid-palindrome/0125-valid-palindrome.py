import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=re.sub(r'[^A-Za-z0-9]','',s)
        a=s[::-1]
        if a==s:
            return True
        else:
            return False