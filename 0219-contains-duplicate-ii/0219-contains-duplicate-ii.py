class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        size=len(nums)
        hm={}
        for i in range(size):
            if nums[i] in hm:
                hm[nums[i]].append(i)
            else:
                hm[nums[i]]=[i]

        for num in hm:
            if len(hm[num])<2:
                continue
            else:
                length=len(hm[num])
                for i in range(length-1):
                    if abs(hm[num][i]-hm[num][i+1])<=k:
                        return True
        return False