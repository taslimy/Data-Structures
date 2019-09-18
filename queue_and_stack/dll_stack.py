import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.storage.add_to_head(value)
  
  def pop(self):
    if len(self.storage) < 1:
      return None
    return self.storage.remove_from_head()

  def len(self):
    return len(self.storage)


# my testsing #
g = Stack()
g.push(1)
g.push(2)
g.push(3)
g.push(4)
g.push(5)
g.push(10)
print(g.storage)
print(g.pop()) #should be 10
