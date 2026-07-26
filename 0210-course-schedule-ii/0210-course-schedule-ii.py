import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        indegree=[0]*numCourses
        adj={i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            indegree[x]+=1
            adj[y].append(x)

        q=collections.deque([i for i in adj if indegree[i]==0])
        ans=[]

        while q:
            node=q.popleft()
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
            ans.append(node)

        if len(ans)!=numCourses:
            return []
        return ans