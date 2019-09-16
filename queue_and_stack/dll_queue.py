import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.storage.add_to_tail(value) # can't use append here only takes 1 value gotta use insert
  
  def dequeue(self):
    if len(self.storage) < 1:
      return None
    return self.storage.remove_from_head()

  def len(self):
    return len(self.storage)

    # python test_queue.py -v
