from Stack import Node

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


