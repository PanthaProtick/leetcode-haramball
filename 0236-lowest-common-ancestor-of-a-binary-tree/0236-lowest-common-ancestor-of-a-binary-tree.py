# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        levels,parents=self.bfs(root)

        if levels[(p)]<levels[(q)]:
            while levels[(q)]>levels[(p)]:
                q=parents[(q)]

        elif levels[(q)]<levels[(p)]:
            while levels[(p)]>levels[(q)]:
                p=parents[(p)]

        if p!=q:
            while p!=q:
                p=parents[(p)]
                q=parents[(q)]
        return p

    def bfs(self, root):
        parents={}
        levels={}
        parents[(root)]=None
        levels[(root)]=0
        queue=deque([root])

        while queue:
            node=queue.popleft()
            level=levels[(node)]
            if node.left:
                parents[(node.left)]=node
                levels[(node.left)]=level+1
                queue.append(node.left)
            if node.right:
                parents[(node.right)]=node
                levels[(node.right)]=level+1
                queue.append(node.right)
        
        return levels,parents