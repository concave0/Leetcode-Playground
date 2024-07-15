from collections import deque
from typing import List, Optional


class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def in_order(self,root) -> List[int]:
    result = []
    if root:
      result.extend(self.in_order(root.left))
      result.append(root.val)
      result.extend(self.in_order(root.right))
    return result  

  def post_order(self, root) -> List[int]:
    result = []
    if root: 
      result.extend(self.post_order(root.left))
      result.extend(self.post_order(root.right))
      result.append(root.val)
    return result  

  def pre_order(self,root) -> List[int]: 
    result = []
    if root: 
      result.append(root.val)
      result.extend(self.pre_order(root.left))
      result.extend(self.pre_order(root.right))
    return result 

  
  def list_to_binary_tree(self, values: List[Optional[int]]):
  
    if not values:
      return None
      
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
      current = queue.popleft()
  
      if i < len(values):
        if values[i] is not None:
          current.left = TreeNode(values[i])
          queue.append(current.left)
        i += 1
  
      if i < len(values):
        if values[i] is not None:
          current.right = TreeNode(values[i])
          queue.append(current.right)
        i += 1 

    return root

  
