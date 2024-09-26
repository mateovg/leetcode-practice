from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
    
    def from_list(self, nums: List[int]) -> 'TreeNode':
        """
        Converts a list of integers into a binary tree.
        Args:
            nums (List[int]): A list of integers to be converted into a binary tree.
        Returns:
            TreeNode: The root node of the resulting binary tree.
        """
        if not nums:
            return None
        root = TreeNode(val=nums[0])
        queue = [root]
        i = 1
        while queue and i < len(nums):
            node = queue.pop(0)
            if nums[i] is not None:
                node.left = TreeNode(val=nums[i])
                queue.append(node.left)
            i += 1
            if i < len(nums) and nums[i] is not None:
                node.right = TreeNode(val=nums[i])
                queue.append(node.right)
            i += 1
        return root 