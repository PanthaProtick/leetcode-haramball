class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions=[(0,-1),(-1,0)]
        rows=len(grid)
        cols=len(grid[0])
        dp=[]
        visited=[]
        
        for i in range(rows):
            arr=[99999999 for j in range(cols)]
            flags=[False for j in range(cols)]
            dp.append(arr)
            visited.append(flags)

        q=collections.deque()
        q.append((rows-1,cols-1))
        visited[rows-1][cols-1]=True
        dp[rows-1][cols-1]=grid[rows-1][cols-1]

        while q:
            curx,cury=q.popleft()
            for a,b in directions:
                x=curx+a
                y=cury+b
                if x>=0 and x<rows and y>=0 and y<cols:
                    dp[x][y]=min(dp[x][y],dp[curx][cury]+grid[x][y])
                    if not visited[x][y]:
                        q.append((x,y))
                        visited[x][y]=True

        return dp[0][0]