# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invert(self, root):
        if not root:
            return None
        else:
            temp1=self.invert(root.left)
            temp2=self.invert(root.right)
            root.left=temp2
            root.right=temp1
            return root

    def isEqual(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)

    def isSymmetric(self, root):
        if not root:
            return True
        self.invert(root.right)
        return self.isEqual(root.left, root.right)