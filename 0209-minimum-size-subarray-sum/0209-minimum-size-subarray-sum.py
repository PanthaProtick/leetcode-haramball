class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        total=nums[0]
        width=0
        size=len(nums)
        if sum(nums)<target:
            return 0
        ans=size
        while j<size and i<size:
            width=j-i+1
            if total>=target:
                ans=min(width,ans)
                if total==target:
                    j+=1
                    if j<size:
                        total+=nums[j]
                total-=nums[i]
                i+=1
            else:
                j+=1
                if j<size:
                    total+=nums[j]
        return ans