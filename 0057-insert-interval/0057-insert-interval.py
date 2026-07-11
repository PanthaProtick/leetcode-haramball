class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        size=len(intervals)
        i=self.lower(intervals, newInterval[0])    
        j=self.higher(intervals, newInterval[1])
        if i==-1 and j==-1:
            return [newInterval]
        elif i==-1:
            if intervals[j][0]>newInterval[1]:
                intervals=intervals[j:]
                intervals.insert(0,newInterval)
                return intervals
            else:
                intervals[j][0]=newInterval[0]
                intervals=intervals[j:]
                return intervals
        elif j==-1:
            if intervals[i][1]<newInterval[0]:
                intervals=intervals[:i+1]
                intervals.append(newInterval)
                return intervals
            else:
                intervals[i][1]=newInterval[1]
                intervals=intervals[:i+1]
                return intervals
        else:
            if intervals[i][1]<newInterval[0] and intervals[j][0]>newInterval[1]:
                intervals=intervals[:i+1]+[newInterval]+intervals[j:]
                return intervals
            elif intervals[i][1]<newInterval[0]:
                intervals[j][0]=newInterval[0]
                intervals=intervals[:i+1]+intervals[j:]
                return intervals
            elif intervals[j][0]>newInterval[1]:
                intervals[i][1]=newInterval[1]
                intervals=intervals[:i+1]+intervals[j:]
                return intervals
            else:    
                 intervals[i][1]=intervals[j][1]
                 intervals=intervals[:i+1]+intervals[j+1:] if j!=size-1 else intervals[:i+1]
                 return intervals   

    def lower(self, intervals, value):
        lp=0
        rp=len(intervals)-1
        ans=-1
        while lp<=rp:
            mid=lp+(rp-lp)//2
            if intervals[mid][0]==value:
                return mid
            elif intervals[mid][0]<value:
                ans=mid
                lp=mid+1
            else:
                rp=mid-1
        return ans

    def higher(self, intervals, value):
        lp=0
        rp=len(intervals)-1
        ans=-1
        while lp<=rp:
            mid=lp+(rp-lp)//2
            if intervals[mid][1]==value:
                return mid
            elif intervals[mid][1]<value:
                lp=mid+1
            else:
                ans=mid
                rp=mid-1
        return ans