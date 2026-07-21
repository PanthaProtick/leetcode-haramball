# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.traversal=self.dfs(root,[])
        self.pointer=-1
        

    def next(self):
        """
        :rtype: int
        """
        self.pointer+=1
        return self.traversal[self.pointer]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer>=len(self.traversal)-1:
            return False
        else:
            return True

    def dfs(self,root,traversed):
        if root:
            if root.left:
                self.dfs(root.left,traversed)
            traversed.append(root.val)
            if root.right:
                self.dfs(root.right,traversed)
        return traversed


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()