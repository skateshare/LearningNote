class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def append(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def prepend(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def outputArray(self):
        res = []
        ptr = self.head
        while ptr != None:
            res.append(ptr.val)
            ptr = ptr.next
        return res

    def traverse(self, index):
        counter = 0
        ptr = self.head
        while True:

            if counter == index:
                break

            ptr = ptr.next
            counter += 1

        return ptr

    def insert(self, index, value):
        ptr = self.traverse(index - 1)
        node = Node(value)
        node.next = ptr.next
        ptr.next = node
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index >= self.length:
            pass
        elif index != 0:
            ptr1 = self.traverse(index - 1)
            ptr2 = self.traverse(index)
            ptr1.next = ptr2.next
            ptr2.next = None
            del ptr2
            self.length -= 1