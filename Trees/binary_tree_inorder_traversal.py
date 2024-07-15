"""
Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


"""

from collections import deque
from typing import Optional, List

from BinaryTree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    self.inorder_helper(root,result=result)
    return result 
    
  
  def inorder_helper(self, node: Optional[TreeNode], result: List[int]):
    if not node: 
      return
  
    self.inorder_helper(node.left, result)
    result.append(node.val)
    self.inorder_helper(node.right, result)
    
          
root1 = [1, None, 2, 3]
Output1 = [1, 3, 2]

root2 = []
Output2 = []

root3 = [1]
Output3 = [1]

s = Solution()
tree1 = TreeNode()
root_node = tree1.list_to_binary_tree(values=root1)
test1 = s.inorderTraversal(root=root_node)
print(test1)
