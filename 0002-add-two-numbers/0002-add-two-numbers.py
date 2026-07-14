# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1=l1
        node2=l2
        carry=0
        total=None
        prev=None
        while l1 or l2:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            res=a+b+carry
            node=ListNode(res%10,None)
            if not total:
                prev=node
                total=node
            else:
                prev.next=node
                prev=node
            carry=int(res/10)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry!=0:
            node=ListNode(carry,None)
            prev.next=node
        return total