from typing import Optional , List

from BinaryTree import TreeNode


"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

"""

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True 
    return self.is_mirror(root.left, root.right)
    
  def is_mirror(self, left: Optional[TreeNode], right: Optional[TreeNode]):
    if not left and not right: 
      return True 
    if not left or not right: 
      return False 
    return (left.val == right.val) and self.is_mirror(left.left, right.right) and self.is_mirror(left.right , right.right)

# root = [1,2,2,3,4,4,3]
root = [1,2,2,None,3,None,3]
expected_output = False

s = Solution()
tree1 = TreeNode()
root_node = tree1.list_to_binary_tree(values=root)
print(s.isSymmetric(root_node))
