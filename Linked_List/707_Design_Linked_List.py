class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(-1)
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1

        dummyHead = self.head
        cur = dummyHead
        for i in range(index+1):
            cur = cur.next
        return cur.val

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        newNode = ListNode(val)
        cur.next = newNode
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index >= self.length + 1:
            return

        cur = self.head
  
        for i in range(index):
            cur = cur.next

        newNode = ListNode(val)
        
        newNode.next = cur.next
        cur.next = newNode

        self.length += 1    
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return

        cur = self.head
        for i in range(index):
            cur = cur.next
        
        if cur.next.next:    
            cur.next = cur.next.next
        else:
            cur.next = None

        self.length -= 1

            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)