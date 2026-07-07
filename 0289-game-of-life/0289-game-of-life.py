class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ans=[]
        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            row=[]
            for j in range(cols):
                live=0
                if j-1>=0:
                    live+=board[i][j-1]
                if j+1<cols:
                    live+=board[i][j+1]
                if i-1>=0:
                    live+=board[i-1][j]
                if i+1<rows:
                    live+=board[i+1][j]
                if j-1>=0 and i-1>=0:
                    live+=board[i-1][j-1]
                if j+1<cols and i+1<rows:
                    live+=board[i+1][j+1]
                if j-1>=0 and i+1<rows:
                    live+=board[i+1][j-1]
                if j+1<cols and i-1>=0:
                    live+=board[i-1][j+1]
                row.append(live)
            ans.append(row)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==0:
                    if ans[i][j]==3:
                        board[i][j]=1
                else:
                    if ans[i][j]<2:
                        board[i][j]=0
                    elif ans[i][j]>3:
                        board[i][j]=0
        return