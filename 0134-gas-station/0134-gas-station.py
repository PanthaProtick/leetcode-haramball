class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        temp=gas
        size=len(gas)
        for i in range(size):
            temp[i]-=cost[i]

        if sum(temp)>=0:
            prefix=[]
            for i in range(size):
                if i==0:
                    prefix.append(0)
                else:
                    prefix.append(prefix[-1]+temp[i-1])
            i=0
            while temp[i]<0:
                i+=1
            k=i+1
            while k<size:
                if temp[k]>=0:
                    if prefix[k]-prefix[i]<0:
                        i=k
                k+=1
            return i
        else:
            return -1


# 1 -3 1 -2 3
# 0 1 -2 -1 -3 0
# -2 -2 -2 3 3
# 0 -2 -4 -6 -3