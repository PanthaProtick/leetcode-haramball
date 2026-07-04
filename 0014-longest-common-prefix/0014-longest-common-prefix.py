class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        s=len(strs[0])
        for i in range(s):
            l=strs[0][i]
            for w in strs[1:]:
                ws=len(w)
                if i>=ws or w[i]!=l:
                    return ans
            ans+=l
        return ans