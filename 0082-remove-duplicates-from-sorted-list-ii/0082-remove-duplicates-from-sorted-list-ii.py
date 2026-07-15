class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        stack=[]
        ignore=None
        while cur:
            if (not stack or cur.val!=stack[-1].val) and cur.val!=ignore:
                if stack:
                    stack[-1].next=cur
                stack.append(cur)
            elif stack and stack[-1].val==cur.val:
                ignore=cur.val
                stack.pop()
                if stack:
                    stack[-1].next=None
            cur=cur.next

        return stack[0] if stack else None