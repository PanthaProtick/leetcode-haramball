class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans = ""
        i = 0
        size = len(strs)

        while i < len(strs[0]):
            if strs[0][i] == strs[size - 1][i]:
                ans += strs[0][i]
            else:
                break
            i += 1

        return ans