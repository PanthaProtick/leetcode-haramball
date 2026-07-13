# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare=head
        turtle=head
        while hare is not None and hare.next is not None:
            turtle=turtle.next
            hare=hare.next.next
            if hare==turtle:
                return True
        return False
            
        