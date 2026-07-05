class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=set()
        size=len(nums)
        nums.sort()
        for i in range(size-1):
            self.twoSum(nums[i+1:],nums[i]*(-1),ans)
            #target=nums[i]*(-1)
            #a=i+1
            #b=size-1
            #if a==b:
                #break
            
        ans2=[]
        for tup in ans:
            a,b,c=tup[0],tup[1],tup[2]
            ans2.append([a,b,c])
        return ans2


    def twoSum(self,nums,target,ans):
        i=0
        j=len(nums)-1
        if i==j:
            return
        while i<j:
            if nums[i]+nums[j]==target:
                ans.add((target*(-1),nums[i],nums[j]))
                i+=1
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        return