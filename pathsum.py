from typing import Optional

from dsa.trees import TreeNode

"""
Given the root of a binary tree and an integer targetSum, 
return the number of paths where the sum of the values along 
the path equals targetSum.

The path does not need to start or end at the root or a leaf, 
but it must go downwards (i.e., traveling only from parent 
nodes to child nodes).
"""


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    prefix_map = {}

    def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
        if not node:
            return 0
        curr_sum += node.val

        paths = 1 if curr_sum == target_sum else 0
        paths += prefix_map.get(curr_sum - target_sum, 0)
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

        if node.left:
            paths += dfs(node.left, curr_sum)
        if node.right:
            paths += dfs(node.right, curr_sum)

        prefix_map[curr_sum] -= 1
        return paths

    return dfs(root, 0)


test_cases = [[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8]
tree = TreeNode().from_list(test_cases[0])
res = path_sum(tree, test_cases[1])
print(res, res == 3)