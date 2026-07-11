class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        i=0
        st=""
        st+=str(nums[i])
        width=0
        size=len(nums)
        ans=[]
        while i<size:
            width+=1
            if i==size-1:
                if width>1:
                    st+=("->")
                    st+=str(nums[i])
                ans.append(st)
                i+=1
                continue
            if nums[i+1]!=nums[i]+1:
                if width>1:
                    st+=("->"+str(nums[i]))
                ans.append(st)
                width=0
                st=str(nums[i+1])
            i+=1
        return ans