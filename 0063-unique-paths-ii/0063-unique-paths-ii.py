class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])

        if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1:
            return 0

        prev_directions=[(-1,0),(0,-1)]
        next_directions=[(1,0),(0,1)]

        dp=[]
        visited=[]

        for i in range(rows):
            arr=[0 for j in range(cols)]
            dp.append(arr)
            visited.append([False for j in range(cols)])

        q=collections.deque()
        q.append((0,0))
        visited[0][0]=True
        dp[0][0]=1

        while q:
            curx,cury=q.popleft()
            total=0
            for a,b in prev_directions:
                x=curx+a
                y=cury+b
                if x>=0 and x<rows and y>=0 and y<cols and obstacleGrid[x][y]==0:
                    total+=dp[x][y]

            dp[curx][cury]=max(dp[curx][cury],total)

            for a,b in next_directions:
                x=curx+a
                y=cury+b
                if x>=0 and x<rows and y>=0 and y<cols and obstacleGrid[x][y]==0 and not visited[x][y]:
                    q.append((x,y))
                    visited[x][y]=True

        return dp[rows-1][cols-1]