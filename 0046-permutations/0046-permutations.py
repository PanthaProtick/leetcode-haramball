class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]

        def backtrack(temp,path):
            if len(temp)==0:
                ans.append(list(path))
                return

            for i in range(len(temp)):
                path.append(temp[i])
                backtrack(temp[:i]+temp[i+1:],path)
                path.pop()

        backtrack(nums,[])
        return ans