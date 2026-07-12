class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        size=len(points)
        ans=1
        start=points[0][0]
        end=points[0][1]
        for i in range(1,size):
            if points[i][0]>end:
                ans+=1
                start=points[i][0]
                end=points[i][1]
            else:
                start=max(start,points[i][0])
                end=min(end,points[i][1])
        return ans
        