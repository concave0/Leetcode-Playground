"""
It supports three operations:

Insert (or "Push"): Putting an item into the stack.
Peek: Look at the top item of the stack (the last inserted item that's not removed).
Remove (or "Pop"): Remove the top item of the stack.

"""

class Stack:
  def __init__(self): 
    self.items = []

  
  def remove(self):
    return self.items.pop() 

  def add(self, item):
    self.items.append(item) 

  def peek(self):
    return self.items[-1]
    