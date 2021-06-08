from Stack import Node
from Stack import Stack3

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0


    def enqueue(self, val):
        temp = Node(val)
        if self.length == 0:
            self.first = temp
            self.last = temp
        else:
            self.last.next = temp
            self.last = temp

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.first
            self.first = None
            self.last = None
            self.length = 0
            return temp
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp

    def peek(self):
        if self.length == 0:
            return None
        else:
            return self.first

# this is to implement Queue using stack
class Queue2():
    def __init__(self):
        self.inQ = Stack3()
        self.outQ = Stack3()
        self.length = 0

    def enqueue(self, val):
        while True:
            if self.outQ.empty() == True:
                break
            self.inQ.push(self.outQ.pop())

        self.inQ.push(val)

    def dequeue(self):
        while True:
            if self.inQ.empty() == True:
                break
            self.outQ.push(self.inQ.pop())
        return self.outQ.pop()

    def peek(self):
        while True:
            if self.inQ.empty() == True:
                break
            self.outQ.push(self.inQ.pop())
        return self.outQ.peek()




