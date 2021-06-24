"""
the benefit of linklist :
prepend and append time complexity>> O(1)  suitable to implement Queue
memory allocation is scattered like dict() but unlike dict() the data in the linklist has order !
unlike static arry , link list has flexible size

cost more memory to (next or pre)
slow lookup
"""


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
        if index > self.length:
            return None
        counter = 0
        ptr = self.head
        while True:

            if counter == index:
                break

            ptr = ptr.next
            counter += 1

        return ptr

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif index > self.length:
            pass
        else:
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

    # change in place
    def reverse(self):

        counter = self.length-1
        ptr = self.head
        pos = self.length
        token = self.tail
        while True:

            if counter == 0:
                break

            self.insert(pos, ptr.val)
            ptr = ptr.next
            counter -= 1

        while True:
            if self.head == token:
                break
            ptr = self.head
            self.head =self.head.next
            ptr.next = None
            del ptr
            self.length -= 1

    # return with another linklist
    def reverse2(self):
        res = LinkList()
        res.append(self.tail.val)
        ptr = self.head
        for i in range(self.length-1):
            res.insert(1, ptr.val)
            ptr = ptr.next
        return res




class BiNode():
    def __init__(self, val = None, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre

class DoubleLinkList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = BiNode(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.pre = self.tail
            self.tail = newNode
        self.length += 1

    def prepend(self,value):
        newNode = BiNode(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.pre = newNode
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
        if index > self.length:
            return None
        counter = 0
        ptr = self.head
        while True:

            if counter == index:
                break

            ptr = ptr.next
            counter += 1

        return ptr

    def Rtraverse(self, index):
        if index >= self.length:
            return None
        counter = self.length -1
        ptr = self.tail
        while True:

            if counter == index:
                break

            ptr = ptr.pre
            counter -= 1

        return ptr


    def insert(self,index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif index > self.length:
            pass

        else:
            ptr = self.traverse(index-1)
            newNode = BiNode(value)
            newNode.next = ptr.next
            ptr.next = newNode
            newNode.next.pre = newNode
            newNode.pre = ptr


    def remove(self, index):
        if index == 0:
            ptr = self.head
            self.head = ptr.next
            self.head.pre = None
            ptr.next = None
            del ptr
            self.length -= 1
        elif index == self.length-1:
            ptr = self.tail
            self.tail = ptr.pre
            self.tail.next = None
            ptr.pre = None
            del ptr
            self.length -= 1
        elif index >= self.length:
            pass
        else:
            ptr = self.traverse(index-1)
            ptr.next.pre = None
            ptr.next = ptr.next.next
            if ptr.next != None:
                ptr.next.pre = ptr
            self.length -= 1





