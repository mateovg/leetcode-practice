from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, next: Optional['TreeNode'] = None) -> None:
        """
        Initializes a ListNode object.

        Args:
            val (int): The value of the node. Defaults to 0.
            next (Optional['ListNode']): The reference to the next node in the list. Defaults to None.
        """
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"TreeNode(val={self.val}, next={self.next})"    
    
    def from_list(self, nums: List[int]) -> 'TreeNode':
        """
        Converts a list of integers into a linked list.
        Args:
            nums (List[int]): A list of integers to be converted into a linked list.
        Returns:
            ListNode: The head node of the resulting linked list.
        """
        root = TreeNode()
        node = root
        for num in nums:
            new_node = TreeNode(val=num)
            node.next = new_node
            node = node.next
        return root.next
            