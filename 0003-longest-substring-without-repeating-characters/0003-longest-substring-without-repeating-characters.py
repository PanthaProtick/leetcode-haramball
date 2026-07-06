class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=len(s)
        if size==0:
            return 0
        chars=set()
        i=0
        j=1
        ans=1
        chars.add(s[0])
        while j<size and i<size:
            width=j-i+1
            if s[j] not in chars:
                chars.add(s[j])
                ans=max(width,ans)
                j+=1
            else:
                if i!=j:
                    chars.remove(s[i])
                    i+=1
                else:
                    j+=1
        return ans