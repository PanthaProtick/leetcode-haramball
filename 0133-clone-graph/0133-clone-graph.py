"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        m={}

        visited=set()
        q=collections.deque()
        q.append(node)
        visited.add(node.val)

        while q:
            cur=q.popleft()
            if cur.val not in m:
                m[cur.val]=Node(cur.val)
            for neighbor in cur.neighbors:
                if neighbor.val not in m:
                    m[neighbor.val]=Node(neighbor.val)
                m[cur.val].neighbors.append(m[neighbor.val])
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    q.append(neighbor)

        return m[node.val]

        
