# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    	# 1. use two stacks.
    	# 2. watch out for sum of two digits more than 10

        s1 = []
        s2 = []

        node = l1
        while node:
            s1.append(node.val)
            node = node.next

        node = l2
        while node:
            s2.append(node.val)
            node = node.next

        head = ListNode()
        while s1 or s2:
            if len(s1) > 0:
                num1 = s1.pop()
            else:
                num1 = 0

            if len(s2) > 0:
                num2 = s2.pop()
            else:
                num2 = 0

            if num1 + num2 <= 9:
                node = ListNode(num1 + num2)
                node.next = head.next
                head.next = node
            else:
                node = ListNode((num1 + num2) % 10)
                node.next = head.next
                head.next = node
                if len(s1) > 0:
                    s1[-1] += 1
                else:
                    s1.append(1)                

        return head.next



