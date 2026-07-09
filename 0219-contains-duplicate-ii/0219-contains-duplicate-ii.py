class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm:
                if i - hm[nums[i]] <= k:
                    return True

            hm[nums[i]] = i

        return False