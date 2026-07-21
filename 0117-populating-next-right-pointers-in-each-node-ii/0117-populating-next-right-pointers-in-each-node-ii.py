"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue=[root]
        traversed=[]
        levels={}
        levels[(root)]=0
        while queue:
            node=queue.pop(0)
            level=levels[(node)]
            if node.left:
                queue.append(node.left)
                levels[(node.left)]=level+1
            if node.right:
                queue.append(node.right)
                levels[(node.right)]=level+1
            traversed.append(node)

        size=len(traversed)
        for i in range(size):
            if i<size-1:
                if levels[(traversed[i])]==levels[(traversed[i+1])]:
                    traversed[i].next=traversed[i+1]
                    continue
            traversed[i].next=None

        return root
            