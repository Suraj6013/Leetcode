# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        # make the middle element the root
        root = TreeNode(nums[mid])

        # left half becomes left subtree
        root.left = self.sortedArrayToBST(nums[:mid])

        # right half becomes right subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root