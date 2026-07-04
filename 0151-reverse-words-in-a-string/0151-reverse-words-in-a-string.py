class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        split=s.split()
        split=split[::-1]
        ans=""

        for word in split:
            ans+=(word+" ")
        
        return ans[:-1]
        