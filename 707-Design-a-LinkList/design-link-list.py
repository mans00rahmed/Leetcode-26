class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):

        current = self.head

        while current.next is not None:
            if current.next.val == index:
                return index
                break
            current = current.next

    def addAtHead(self, value):
        new_node = Node(value)
        new_node.next = self.head

    def addAtTail(self, value):
        # make a new instering node
        current = self.head
        new_node = Node(value)
        while current.next is not None:
            current = current.next
        current.next = new_node

    def addAtIndex(self, value):
        new_node = Node(value)
        current = self.head
        while current.next.val <= value:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def deleteFromTail(self):
        current = self.head
        if self.head is None or self.head.next is None:
            self.head = None
            return
        while current.next is not None:
            current = current.next
        current = None

    def deleteHead(self):
        if self.head.next:
            self.head = self.head.next
        else:
            return

    def deleteAtIndex(self, index):
        if index == 1:
            self.deleteHead()
            return

        position = 1

        current = self.head

        while current.next is not None:
            if position == index-1:
                break
            current = current.next
            position += 1

        current.next = current.next.next


# :Driver Code
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtIndex(2.5)
    ll.deleteAtIndex(5)

    # print the list to check
    current = ll.head
    while current is not None:
        print(current.val)
        current = current.next
