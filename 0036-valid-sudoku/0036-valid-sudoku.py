class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]

        for i in range(9):
            for j in range(9):
                number=board[i][j]
                if number==".":
                    continue
                if number in rows[i] or number in cols[j] or number in squares[i//3][j//3]:
                    return False
                
                rows[i].add(number)
                cols[j].add(number)
                squares[i//3][j//3].add(number)
        return True