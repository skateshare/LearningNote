from Stack import Stack3
from Queue import Queue
from Queue import Queue2
from Tree import Tree
from Graph import Graph
from LinkList import LinkList
from LinkList import DoubleLinkList

print("======test linklist======")
myList = LinkList()
myList.append(3)
myList.append(1)
myList.append(2)
myList.append(4)
myList.append(8)
print(myList.outputArray())
myList.reverse()
print(myList.outputArray())




test = myList.reverse2()
print(test.outputArray())



myList2 = DoubleLinkList()
myList2.append(3)
myList2.append(1)
myList2.append(2)
myList2.append(4)
myList2.append(8)
myList2.prepend(10)
myList2.prepend(15)
myList2.prepend(110)
myList2.prepend(101)
print(myList2.outputArray())
myList2.remove(3)
print(myList2.outputArray())
print(myList2.Rtraverse(3).val)





print("======test stack use array======")
october = Stack3()
october.push("google")
october.push("netflix")
october.push("repl")
print(october.peek())
print(october.pop())
print(october.peek())
october.push("ptt")
print(october.peek())


print("======test Queue use two stacks======")
line = Queue2()
line.enqueue("October")
line.enqueue("Clay")
line.enqueue("Leo")
print(line.dequeue())
print(line.peek())
print(line.dequeue())
print(line.peek())



print("======test Tree with remove method======")
myTree = Tree()
myTree.insert(50)
myTree.insert(40)
myTree.insert(70)
myTree.insert(45)
myTree.insert(43)
myTree.insert(47)
myTree.insert(46)
myTree.insert(48)
#print(myTree.preorderTraversal())
myTree.remove(47)
print(myTree.preorderTraversal())

print("======test Graph========")
myGraph = Graph();
myGraph.addVertex('0');
myGraph.addVertex('1');
myGraph.addVertex('2');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');
myGraph.addEdge('3', '1');
myGraph.addEdge('3', '4');
myGraph.addEdge('4', '2');
myGraph.addEdge('4', '5');
myGraph.addEdge('1', '2');
myGraph.addEdge('1', '0');
myGraph.addEdge('0', '2');
myGraph.addEdge('6', '5');

myGraph.showConnections();
