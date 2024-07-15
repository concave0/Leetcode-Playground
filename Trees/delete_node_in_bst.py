"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.If the node is found, delete the node.

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
"""

from collections import deque
from typing import Optional

from BinaryTree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
      
      if root is None: 
        return None 
        
      queue = deque([root])
      count = 0 
      while len(queue) > 0: 
        curr = queue.popleft()
        if curr.val[count] != key: 
          print("inside of else")
          curr.val[count] = None
        else: 
          pass 
      return queue[0].val
        
          
root = [5,3,6,2,4,None,7], 
key = 3
# expected_output = [5,4,6,2,None,None,7]
tree = TreeNode()
root_node = tree.list_to_binary_tree(values=root)

s = Solution()
result = s.deleteNode(root=root_node, key=key)
print(result)


