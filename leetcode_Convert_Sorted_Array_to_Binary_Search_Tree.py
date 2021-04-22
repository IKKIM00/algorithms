# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        node = TreeNode()

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            node.val = nums[0]
            return node

        mid = len(nums) // 2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid + 1:])

        node.val = nums[mid]
        node.left = left
        node.right = right

        return node