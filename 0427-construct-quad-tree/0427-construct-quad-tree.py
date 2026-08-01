class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def divide(n,r,c):
            val=grid[r][c]
            isSame=True
            for i in range(r,n+r):
                for j in range(c,n+c):
                    if grid[i][j]!=val:
                        isSame=False
                        break

            if isSame:
                return Node(val,isLeaf=True)

            n=n//2
            root=Node(True,False)
            root.topLeft=divide(n,r,c)
            root.topRight=divide(n,r,c+n)
            root.bottomLeft=divide(n,r+n,c)
            root.bottomRight=divide(n,r+n,c+n)
            return root
        return divide(len(grid),0,0)