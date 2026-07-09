class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx={}
        i=0
        j=len(nums)-1
        for n in range(j+1):
            if nums[n] in idx:
                idx[nums[n]].append(n)
            else:
                idx[nums[n]]=[n]
        nums.sort()
        while i<j:
            if nums[i]+nums[j]==target:
                x=idx[nums[i]][0]
                size=len(idx[nums[j]])
                for n in range(size):
                    if idx[nums[j]][n]!=x:
                        return [x,idx[nums[j]][n]]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1