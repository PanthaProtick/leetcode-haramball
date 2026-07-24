class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols=len(board), len(board[0])
        visited=set()

        def bfs(i,j):
            q=collections.deque()
            q.append((i,j))
            visited.add((i,j))
            directions=[(-1,0),(1,0),(0,-1),(0,1)]

            while q:
                a,b=q.popleft()
                for v,h in directions:
                    anew,bnew=a+v,b+h
                    if anew>=0 and anew<rows and bnew>=0 and bnew<cols and board[anew][bnew]=='O' and (anew,bnew) not in visited:
                        visited.add((anew,bnew))
                        q.append((anew,bnew))
            return

        for j in range(cols):
            if board[0][j]=='O' and (0,j) not in visited:
                bfs(0,j)

        for j in range(cols):
            if board[rows-1][j]=='O' and (rows-1,j) not in visited:
                bfs(rows-1,j)

        for i in range(rows):
            if board[i][0]=='O' and (i,0) not in visited:
                bfs(i,0)

        for i in range(rows):
            if board[i][cols-1]=='O' and (i,cols-1) not in visited:
                bfs(i,cols-1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and (i,j) not in visited:
                    board[i][j]='X'

        return