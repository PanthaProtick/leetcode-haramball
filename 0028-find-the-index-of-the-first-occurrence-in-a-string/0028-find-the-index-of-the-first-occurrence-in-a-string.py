class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        sizeh=len(haystack)
        sizen=len(needle)
        i=0
        while i<sizeh:
            if haystack[i]==needle[0]:
                j=i+sizen
                if j<=sizeh and haystack[i:j]==needle:
                    return i
            i+=1
        return -1
        