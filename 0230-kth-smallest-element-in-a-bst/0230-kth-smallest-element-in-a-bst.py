# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        traversal=[]
        self.dfs(root, traversal)
        return traversal[k-1]
    
    def dfs(self, root, traversal):
        if not root:
            return traversal
        if root.left:
            self.dfs(root.left,traversal)
        traversal.append(root.val)
        if root.right:
            self.dfs(root.right,traversal)
        return