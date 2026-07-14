"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cur=head
        map={}
        idx=0
        nodeArr=[]
        prev=None
        while cur:
            map[(cur)]=idx
            idx+=1
            node=Node(x=cur.val)
            nodeArr.append(node)
            if prev:
                prev.next=node
            prev=node
            cur=cur.next

        cur=head
        temp=nodeArr[0]
        while cur and temp:
            temp.random=nodeArr[map[(cur.random)]] if cur.random else None 
            temp=temp.next
            cur=cur.next
        return nodeArr[0]