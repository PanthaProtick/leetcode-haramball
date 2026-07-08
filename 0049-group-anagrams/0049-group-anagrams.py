class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans={}
        for word in strs:
            s=tuple(sorted(word))
            if s in ans:
                ans[s].append(word)
            else:
                ans[s]=[word]

        return list(ans.values())