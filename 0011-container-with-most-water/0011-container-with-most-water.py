class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size=len(height)
        i=0
        j=size-1
        ans=0
        while i<j:
            area=(j-i)*min(height[i],height[j])
            if area>ans:
                ans=area
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            else:
                leftdiff=height[i+1]-height[i]
                rightdiff=height[j-1]-height[j]
                if leftdiff>rightdiff:
                    i+=1
                else:
                    j-=1
        return ans