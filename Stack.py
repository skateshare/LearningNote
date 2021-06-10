from LinkList import *


# stack use LinkList
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



# stack use node
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

    def empty(self):
        if self.length <= 0:
            return True
        else:
            return False



# stack use array
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

    def empty(self):
        if len(self.arr) <= 0:
            return True
        else:
            return False

