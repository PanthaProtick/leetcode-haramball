# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        stack=[None]
        cur=head
        while cur:
            stack.append(cur)
            cur=cur.next

        prev=None
        temp=None
        for i in range(n+1):
            prev=stack.pop()
            if prev:
                temp=prev.next
        if prev:
            prev.next=prev.next.next
            return head
        else:
            return temp