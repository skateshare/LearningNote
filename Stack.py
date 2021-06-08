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



class Stack():
    def __init__(self):
        self.linklist = LinkList()
        self.length = 0

    def peek(self):
        if self.length == 0:
            print("None")
            return None

        else:
            print(self.linklist.tail.val)
            return self.linklist.tail.val

    def push(self, value):
        temp = Node(value)
        if self.length == 0:
            self.linklist.head = temp
            self.linklist.tail = temp
        else:
            self.linklist.append(value)

        self.length += 1

    def pop(self):
        if self.length >= 2:
            pos = self.linklist.traverse(self.length - 2)
            temp = self.linklist.tail.val
            self.linklist.tail = pos
            self.length -= 1
            print(temp)
            return temp
        elif self.length == 1:
            temp = self.linklist.head.val
            self.linklist.head = None
            self.linklist.tail = None
            self.length -= 1
            print(temp)
            return temp
        else:
            print("None")
            return None



# here see another method !
class Stack2():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        temp = Node(value)
        if self.length == 0:
            self.top = temp
            self.bottom = temp
        else:
            temp.next = self.top
            self.top = temp
        self.length += 1

    def pop(self):
        if self.length == 0:
            return self.top
        elif self.length == 1:
            res = self.top
            self.top = None
            self.bottom = None
            self.length -= 1
            return res
        else:
            res = self.top
            self.top = self.top.next
            res.next = None
            self.length -= 1
            return res

    def peek(self):
        return self.top



# in this case , I'll try to use array to implement stack
class Stack3():
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        if len(self.arr) == 0:
            return None
        else:
            res = self.arr[-1]
            del self.arr[-1]
            return res

    def peek(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[-1]

