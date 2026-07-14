# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3=None
        prev=None
        a=list1
        b=list2
        while a or b:
            if ((a and b) and (a.val<=b.val)) or (a and not b):
                x=a.val
                a=a.next
                node=ListNode(x, None)
            elif ((a and b) and (b.val<a.val)) or (b and not a):
                x=b.val
                b=b.next
                node=ListNode(x, None)
            if not prev:
                list3=node
                prev=node
            else:
                prev.next=node
                prev=node
        return list3