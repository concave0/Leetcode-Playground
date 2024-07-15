"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

from BinaryTree import TreeNode


class Solution:
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
      return []
    
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.val == val:
          return [curr.left.val, curr.right.val, curr.val] 
        if curr.left: 
          queue.append(curr.left)
        if curr.right:
          queue.append(curr.right)
    return [] 
    

root = [4, 2, 7, 1, 3]
val = 2
Output = [2, 1, 3]

tree = TreeNode()
root_node = tree.list_to_binary_tree(values=root)

s = Solution()
result = s.searchBST(root=root_node, val=val)
print(result)
