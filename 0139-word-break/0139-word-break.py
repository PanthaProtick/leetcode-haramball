class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size=len(s)
        wordDict=set(wordDict)
        arr=[False for i in range(size+1)]
        arr[0]=True
        for i in range(1,size+1):
            idx=i-1
            for word in wordDict:
                x=i-len(word)
                if x>=0 and arr[x] and s[x:idx+1] in wordDict:
                    arr[i]=True
        return arr[size]