# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
import collections as c
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)