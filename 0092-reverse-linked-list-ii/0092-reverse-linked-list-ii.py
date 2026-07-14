# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        stack=[]
        start=None
        end=None
        cur=head
        entry=False
        pos=0
        while cur:
            pos+=1
            if pos==left:
                entry=True
            if entry:
                stack.append(cur)
            if pos==right:
                entry=False
                end=cur.next
                break
            if not entry:
                start=cur
            cur=cur.next
        if not start:
            start=stack.pop()
            head=start
        while start and stack:
            start.next=stack.pop()
            start=start.next

        if start:
            start.next=end
        return head