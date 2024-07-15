# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


"""
from typing import Optional

from BinaryTree import TreeNode

class Solution:
    def __init__(self) -> None:
        self.left_depth = 0
        self.left_depth = 0 
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs_count(root=root) 

    def dfs_count(self, root):
        if root is None:
            return 0 
        else: 
            if root.left is not None:     
                self.left_depth = self.dfs_count(root.left)
                
            if root.right is not None:
                self.right_depth = self.dfs_count(root.right)
                
        return max(self.left_depth, self.left_depth) + 1
    
s = Solution()
tree = TreeNode()

# Problem One 
root1 = [3,9,20,None,None,15,7]
Output1 = 3

tree1 = tree.list_to_binary_tree(root1)

result1 = s.maxDepth(tree1)
print(result1)
print(result1==Output1)


# Problem Two
root2 = [1,None,2]
Output2 = 2

tree2 = tree.list_to_binary_tree(root2)
print(s.maxDepth(tree2)==Output2)


