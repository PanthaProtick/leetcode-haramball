class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size=len(gas)
        for i in range(size):
            gas[i]-=cost[i]

        if sum(gas)>=0:
            prefix=[]
            for i in range(size):
                if i==0:
                    prefix.append(0)
                else:
                    prefix.append(prefix[-1]+gas[i-1])
            i=0
            while gas[i]<0:
                i+=1
            k=i+1
            while k<size:
                if gas[k]>=0:
                    if prefix[k]-prefix[i]<0:
                        i=k
                k+=1
            return i
        else:
            return -1