class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False


    def deleteNode(self, node):
        if self.head == node and self.tail == Node:
            self.head = None
            self.tail = None
            return
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        return


    def insertBefore(self, nodeToInsert, node):
        while node is not None:
            nodeToInsert.next = node
            nodeToInsert.prev = node.prev
            node.prev.next = nodeToInsert
            node.prev =  nodeToInsert
        return

    def insertAfter(self,nodeToInsert,node):
        while node is not None:
            self.tail = nodeToInsert
            nodeToInsert.prev = node
            node.next = nodeToInsert
            nodeToInsert.next = None
        return






ll1 = DoubleLinkedList()

node1 = Node(2)
node1.in


