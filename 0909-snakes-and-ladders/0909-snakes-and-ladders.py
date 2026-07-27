class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length=len(board)

        def squareToPos(square):
            idx = square - 1
            
            r_from_bottom = idx // length

            c = idx % length
            
            r = length - 1 - r_from_bottom

            if r_from_bottom % 2 == 1:
                c = length - 1 - c
                
            return (r, c)

        q=collections.deque()
        q.append([1,0])
        visited=set()
        visited.add(1)

        while q:
            square,moves=q.popleft()
            for i in range(1,7):
                newSquare=square+i
                x,y=squareToPos(newSquare)
                if board[x][y]!=-1:
                    newSquare=board[x][y]
                if newSquare==length*length:
                    return moves+1
                if newSquare not in visited:
                    q.append([newSquare,moves+1])
                    visited.add(newSquare)

        return -1
        