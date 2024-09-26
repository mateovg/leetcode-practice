import unittest
from dsa.linkedlist import TreeNode

class TestListNode(unittest.TestCase):
    def test_from_list_empty(self):
        # Test with an empty list
        head = TreeNode().from_list([])
        self.assertIsNone(head)

    def test_from_list_single_element(self):
        # Test with a single element list
        head = TreeNode().from_list([1])
        self.assertIsNotNone(head)
        self.assertEqual(head.val, 1)
        self.assertIsNone(head.next)

    def test_from_list_multiple_elements(self):
        # Test with a multiple elements list
        head = TreeNode().from_list([1, 2, 3])
        self.assertIsNotNone(head)
        self.assertEqual(head.val, 1)
        self.assertIsNotNone(head.next)
        self.assertEqual(head.next.val, 2)
        self.assertIsNotNone(head.next.next)
        self.assertEqual(head.next.next.val, 3)
        self.assertIsNone(head.next.next.next)

if __name__ == '__main__':
    unittest.main()