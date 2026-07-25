class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree=[0]*numCourses
        adj={i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            indegree[x]+=1
            adj[y].append(x)

        processed=0

        q=collections.deque([i for i in range(numCourses) if indegree[i]==0])

        while q:
            node=q.popleft()
            processed+=1
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        return processed==numCourses       