class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=-99999
        total=0
        lp=rp=0
        size=len(nums)

        while rp<size:
            total+=nums[rp]
            rp+=1
            ans=max(ans,total)
            if total<0:
                total=0
                lp=rp
            

        return ans