from collections import deque
from typing import List, Optional
from BinaryTree import TreeNode, list_to_binary_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""" 
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightside = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()

                # If this is the right-most node at this level
                if i == level_length - 1:
                    rightside.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside


# Testing the updated solution
root1 = [1, 2, 3, None, 5, None, 4]
root2 = [1, None, 3]
root3 = []

solution = Solution()
print(solution.rightSideView(list_to_binary_tree(root1)))  # Output: [1, 3, 4]
print(solution.rightSideView(list_to_binary_tree(root2)))  # Output: [1, 3]
print(solution.rightSideView(list_to_binary_tree(root3)))  # Output: []
