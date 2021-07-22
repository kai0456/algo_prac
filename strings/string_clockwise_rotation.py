class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	prev = ListNode(None)

    	while head:
    		nextNode = head.next

    		head.next = prev
    		prev = head
    		head = nextNode

    	return prev

