# Assignment
# Build a small binary tree and write three recursive functions: count leaf
# nodes, print an in-order traversal (left, root, right), and search for an
# integer value anywhere in the tree. Demonstrate all three on the sample tree.
#
# Solution


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Sample tree: root 10; left subtree 5 with children 2 and 7; right child 15.
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)


# node is the current subtree root. A leaf has no children; internal nodes
# delegate to their left and right subtrees and combine the results.
def count_leaves(node) -> int:

    # Empty link contributes no leaves.
    if node is None:
        return 0
    # Both children missing: this node is a leaf.
    elif node.left is None and node.right is None:
        return 1
    else:
        # Sum leaf counts from the left and right subtrees.
        return count_leaves(node.left) + count_leaves(node.right)


def inorder_traversal(node):

    # Nothing to visit below a missing link.
    if node is None:
        return

    # Visit left subtree first, then the current value, then the right subtree.
    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)


def search_element(node, element: int) -> bool:

    if node is None:
        return False
    elif node.data == element:
        return True
    else:
        # Value may sit in either subtree; or combines the two Boolean results.
        return search_element(node.left, element) or search_element(node.right, element)


# Leaves are 2, 7, and 15 (three nodes with no children).
print(f"Leaf count: {count_leaves(root)}")
print("In-order:", end=" ")
inorder_traversal(root)
print()
print(f"search_element(root, 7) = {search_element(root, 7)}")
print(f"search_element(root, 99) = {search_element(root, 99)}")
