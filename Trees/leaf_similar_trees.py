from typing import List, Optional

from BinaryTree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].


"""


class Solution:
  def leafSimilar(self, root1: Optional[TreeNode],root2: Optional[TreeNode]) -> bool:
    leaf1 = self.pre_order(root1)
    leaf2 = self.pre_order(root2)
    return leaf1 == leaf2

  def pre_order(self,root) -> List[int]: 
    result = []
    if root:
      if not root.left and not root.right: 
        result.append(root.val)
      result.extend(self.pre_order(root.left))
      result.extend(self.pre_order(root.right))
    return result 
    
s = Solution()
tree = TreeNode()

# Problem one 
rooted1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
rooted2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

tree1 = tree.list_to_binary_tree(rooted1)
tree2 = tree.list_to_binary_tree(rooted2)
print(s.leafSimilar(root1=tree1, root2=tree2))  # Expected Output: true

# Problem two 
rooted3 = [1,2,3]
rooted4 = [1,3,2]

tree3 = tree.list_to_binary_tree(rooted3)
tree4 = tree.list_to_binary_tree(rooted4) # Output: false
print(s.leafSimilar(root1=tree3, root2=tree4))



