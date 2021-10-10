# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def pushStack(node):
            s = []

            while node:
                s.append(node.val)
                node = node.next
            return s

        s1 = pushStack(l1)
        s2 = pushStack(l2)


        head = ListNode()
        while s1 or s2:
            num1, num2 = float(-inf), float(-inf)
            if s1:
                num1 = s1[-1]
            if s2:
                num2 = s2[-1]

            # at least one stack not empty
            if num1 >= num2:
                node = ListNode(s1.pop())
                node.next = head.next
                head.next = node
            else:
                node = ListNode(s2.pop())
                node.next = head.next
                head.next = node                

        return head.next

