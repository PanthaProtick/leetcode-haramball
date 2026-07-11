class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        size=len(intervals)
        i=1
        start=intervals[0][0]
        end=intervals[0][1]
        ans=[]
        while i<size:
            if intervals[i][0]>end:
                ans.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            else:
                end=max(end,intervals[i][1])
            i+=1
        ans.append([start,end])
        return ans
