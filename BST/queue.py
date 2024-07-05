from collections import deque 



"""
Insert (or "Push"): Putting an item into the end of the queue.
Peek: Look at the first item of the queue.
Remove (or "Pop"): Remove the first item of the queue.

"""
class Queue: 
  def __init__(self): 
    self.queue = deque() 

  def add(self,data): 
    self.queue.append(data)   

  def remove_begin(self):
    self.queue.popleft() 

  def peek(self):
    return self.queue[0]  

  def remove_end(self):
    self.queue.pop()
    
  def size(self):
    return len(self.queue)





