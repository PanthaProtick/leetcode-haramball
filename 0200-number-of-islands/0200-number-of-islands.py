from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m=len(grid)
        n=len(grid[0])
        ans=0
        visited=set()

        def bfs(i,j):
            queue=deque([(i,j)])
            visited.add((i,j))
            directions=[(1,0),(-1,0),(0,-1),(0,1)]
            while queue:
                a,b=queue.popleft()
                for v,h in directions:
                    new_a=a+v
                    new_b=b+h
                    if new_a in range(m) and new_b in range(n) and grid[new_a][new_b]=='1' and (new_a,new_b) not in visited:
                        visited.add((new_a,new_b))
                        queue.append((new_a,new_b))
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=='1':
                    bfs(i,j)
                    ans+=1

        return ans