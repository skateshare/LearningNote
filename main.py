from Stack import Stack3
from Queue import Queue



"""october = Stack3()
october.push("google")
october.push("netflix")
october.push("repl")
print(october.peek())
print(october.pop())
print(october.peek())
october.push("ptt")
print(october.peek())"""

line = Queue()

line.enqueue("October")
line.enqueue("Leo")
line.enqueue("Clay")
print(line.peek().val)
line.dequeue()
print(line.peek().val)

