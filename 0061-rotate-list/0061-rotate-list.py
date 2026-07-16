# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        size=0
        cur=head
        while cur:
            size+=1
            cur=cur.next
        
        k%=size
        if k==0:
            return head
        cur=head
        for i in range(size-k-1):
            cur=cur.next
        temp=cur.next
        cur.next=None

        cur=temp
        while cur.next:
            cur=cur.next
        cur.next=head
        return temp