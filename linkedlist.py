from typing import List 

class Node: 
  def __init__(self,data): 
    self.data = data
    self.next = None 
    
class LinkedList: 
  def __init__(self) -> None:
    self.head = None
    self.tail = None 
    self.size = 0 

  def insert_at_beginning(self, data): 
    if data == None: 
      node = Node(data)
      self.head = node 
    else: 
      node = Node(data) 
      node.tail = self.head
      self.head = node 

  def print_list(self): 
    if self.head == None: 
      print("Empty")
    else: 
      temp = self.head 
      while temp != None: 
        print(temp.data)
        temp = temp.next 


llist = LinkedList() 
llist.insert_at_beginning(1) 
llist.insert_at_beginning(2) 
print(llist.print_list())
      
      
      
    