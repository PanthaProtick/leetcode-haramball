class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        num=list(s)
        num.sort()
        size=len(num)
        i=0
        ans=0
        width=0
        while i<size:
            width+=1
            if i==size-1:
                ans=max(width,ans)
                break
            if num[i]+1!=num[i+1]:
                ans=max(width,ans)
                width=0
            i+=1
        return ans