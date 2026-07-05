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
            target=nums[i]*(-1)
            a=i+1
            b=size-1
            if a==b:
                break
            while a<b:
                if nums[a]+nums[b]==target:
                    ans.add((nums[i],nums[a],nums[b]))
                    a+=1
                elif nums[a]+nums[b]>target:
                    b-=1
                else:
                    a+=1
        ans2=[]
        for tup in ans:
            a,b,c=tup[0],tup[1],tup[2]
            ans2.append([a,b,c])
        return ans2