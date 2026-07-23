# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        traversal=[]
        self.dfs(root, traversal)
        size=len(traversal)
        for i in range(size-1):
            if traversal[i]>=traversal[i+1]:
                return False
        return True
        
    
    def dfs(self, root, traversal):
        if not root:
            return traversal
        if root.left:
            self.dfs(root.left,traversal)
        traversal.append(root.val)
        if root.right:
            self.dfs(root.right,traversal)
        return