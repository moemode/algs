"""This module implements a binary tree."""

from __future__ import annotations
from typing import Any, Optional


def height(n: Optional[BinaryNode]) -> int:
    if n:
        return n.height
    else:
        return -1


class BinaryNode:
    """
    A class representing a node in a binary tree.

    Attributes:
        item: The value stored in the node.
        left: The left child of the node.
        right: The right child of the node.
        parent: The parent of the node.
    """

    def __init__(self, x: Any):
        self.item = x
        self.height: int = -1
        self.left: Optional[BinaryNode] = None
        self.right: Optional[BinaryNode] = None
        self.parent: Optional[BinaryNode] = None
        self.subtree_update()

    def subtree_update(self) -> None:
        self.height = 1 + max(height(self.left), height(self.right))

    def skew(self) -> int:
        return height(self.right) - height(self.left)

    def subtree_iter(self):
        """
        Generator function that yields
        all nodes in the subtree rooted at the current node.

        Yields:
            Node: The next node in the subtree.
        """
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    def successor(self):
        if self.right:
            return self.right.subtree_first()
        ancestor = self
        while ancestor.parent and ancestor.parent.right == ancestor:
            ancestor = ancestor.parent
        return ancestor

    def predecessor(self):
        if self.left:
            return self.left.subtree_last()
        ancestor = self
        while ancestor.parent and ancestor.parent.left == ancestor:
            ancestor = ancestor.parent
        return ancestor

    def subtree_insert_before(self, new: BinaryNode):
        if not self.left:
            self.left = new
            new.parent = self
            self.maintain()
        else:
            predecessor = self.left.subtree_last()
            # walked right as far as possible -> predecessor.right == None
            predecessor.right = new
            new.parent = predecessor
            predecessor.maintain()

    def subtree_insert_after(self, new: BinaryNode):
        if not self.right:
            self.right = new
            new.parent = self
            self.maintain()
        else:
            successor = self.right.subtree_first()
            successor.left = new
            new.parent = successor
            successor.maintain()

    def is_leaf(self):
        return self.left is None and self.right is None

    def swap(self, other: BinaryNode) -> None:
        """
        Swaps the values and attributes of two BinaryNodes.

        Args:
            other (BinaryNode): The BinaryNode to swap with.

        Returns:
            None
        """
        item, height, left, right, parent = (
            self.item,
            self.height,
            self.left,
            self.right,
            self.parent,
        )
        self.item, self.height, self.left, self.right, self.parent = (
            other.item,
            other.height,
            other.left,
            other.right,
            other.parent,
        )
        other.item, other.height, other.left, other.right, other.parent = (
            item,
            height,
            left,
            right,
            parent,
        )

    def subtree_delete(self):
        if self.left or self.right:
            if self.left:
                lower_node = self.predecessor()
            else:
                lower_node = self.successor()
            lower_node.item, self.item = self.item, lower_node.item
            return lower_node.subtree_delete()
        # self is leaf
        if self.parent:
            if self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None
            self.parent.maintain()
        return self

    def subtree_rotate_right(self):
        D = self
        B = D.left
        if B is None:
            raise ValueError(
                "Cannot perform right rotation on a node without a left child."
            )
        C = B.right
        B.parent = D.parent
        B.right = D
        D.parent = B
        D.left = C
        if C:
            C.parent = D
        D.subtree_update()
        B.subtree_update()

    def subtree_rotate_left(self):
        B = self
        D = B.right
        if D is None:
            raise ValueError(
                "Cannot perform left rotation on a node without a right child."
            )
        C = D.left
        D.parent = B.parent
        D.left = B
        B.parent = D
        B.right = C
        if C:
            C.parent = B
        B.subtree_update()
        D.subtree_update()

    def rebalance(self):
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left()
        elif self.skew() == -2:
            if self.left.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):
        self.rebalance()
        self.subtree_update()
        if self.parent:
            self.parent.maintain()

    def __str__(self) -> str:
        return self.subtree_2d()

    def subtree_2d(self, space=0, LEVEL_SPACE=5) -> str:
        out = ""
        space += LEVEL_SPACE
        if self.right:
            out = self.right.subtree_2d(space)
        out += " " * len(range(LEVEL_SPACE, space))
        out += ("|" + str(self.item) + "|<") + "\n"
        if self.left:
            out += self.left.subtree_2d(space)
        return out


class BinaryTree:
    """
    Represents a binary tree data structure.

    Attributes:
        root (Optional[BinaryNode]): The root node of the binary tree.
        size (int): The number of nodes in the binary tree.
        node_type (type): The type of nodes in the binary tree.
    """

    def __init__(self, node_type=BinaryNode):
        self.root: Optional[node_type] = None
        self.size = 0
        self.node_type = node_type

    def __len__(self):
        """
        Returns the number of nodes in the binary tree.

        Returns:
            int: The number of nodes in the binary tree.
        """
        return self.size

    def __iter__(self):
        """
        Returns an iterator that iterates over the nodes in the binary tree.

        Yields:
            BinaryNode: The next node in the binary tree.
        """
        if self.root:
            for n in self.root.subtree_iter():
                yield n

    def __str__(self) -> str:
        if not self.root:
            return "<empty>"
        else:
            return self.root.__str__()


def construct_binary_tree(seq: list[Any]) -> BinaryTree:
    """
    Constructs a binary tree from the given list of items A.

    The tree constructed ensures:
    1. The item stored in the ith node of T's traversal order is item ai.
    2. The tree has height O(log n).

    Args:
        A (List): List of items to be stored in the binary tree nodes.

    Returns:
        BinaryTree: The constructed binary tree.
    """
    root = construct_binary_tree_rec(seq, 0, len(seq))
    b = BinaryTree()
    b.root = root
    b.size = len(seq)
    return b


def construct_binary_tree_rec(seq: list[Any], l, r) -> Optional[BinaryNode]:
    # recursively construct binary tree from items in A[l:r]
    if l >= r:
        return None
    c = (l + r) // 2
    root = BinaryNode(seq[c])
    if l < c:
        root.left = construct_binary_tree_rec(seq, l, c)
        root.left.parent = root
    if c + 1 < r:
        root.right = construct_binary_tree_rec(seq, c + 1, r)
        root.right.parent = root
    return root


class BSTNode(BinaryNode):

    left: BSTNode
    right: BSTNode

    def subtree_find(self, k) -> Optional[BSTNode]:
        # find node storing k else find predecessor
        if k == self.item.key:
            return self
        if k < self.item.key:
            subtree = self.left
        if k > self.item.key:
            subtree = self.right
        if subtree:
            return subtree.subtree_find(k)
        else:
            return None

    def subtree_find_next(self, k):
        # find k if its in tree or its predecessor in traversal order
        if self.item.key <= k:
            if self.right:
                return self.right.subtree_find_next(k)
            else:
                return None
        elif self.left:
            n = self.left.subtree_find_next(k)
            if n:
                return n
        return self

    def subtree_find_prev(self, k):
        if self.item.key >= k:
            # if prev exists it is in left subtree
            if self.left:
                return self.left.subtree_find_prev(k)
            else:
                return None
        # self.item.key < k
        elif self.right:
            n = self.right.subtree_find_prev(k)
            if n:
                return n
        return self

    def subtree_insert(self, new_node):
        if new_node.item.key < self.item.key:
            if self.left:
                self.left.subtree_insert(new_node)
            else:
                self.subtree_insert_before(new_node)
        if new_node.item.key > self.item.key:
            if self.right:
                self.right.subtree_insert(new_node)
            else:
                self.subtree_insert_after(new_node)
        else:
            self.item = new_node.item


class SetBinaryTree(BinaryTree):
    """
    Implementation of a Binary Search Tree (BST) that represents a set of unique elements.
    Inherits from Binary_Tree.
    """

    root: Optional[BSTNode]

    def __init__(self):
        """
        Initialize the Set_Binary_Tree object.
        """
        super().__init__(BSTNode)

    def iter_order(self):
        """
        Perform an iterative inorder traversal of the tree.

        Yields:
            Node: Nodes in the tree in inorder traversal.
        """
        yield from self

    def build(self, X: Any):
        """
        Build the tree by inserting elements from the iterable X.

        Args:
            X (iterable): An iterable collection of elements to be inserted into the tree.
        """
        for x in X:
            self.insert(x)

    def find_min(self):
        """
        Find and return the minimum element in the tree.

        Returns:
            Any: The minimum element in the tree.
        """
        if not self.root:
            raise ValueError("Tree is empty, cannot find minimum element.")
        return self.root.subtree_first().item

    def find_max(self):
        """
        Find and return the maximum element in the tree.

        Returns:
            Any: The maximum element in the tree.
        """
        if not self.root:
            raise ValueError("Tree is empty, cannot find maximum element.")
        return self.root.subtree_last().item

    def find(self, k):
        """
        Find an element with key k in the tree and return it if found.

        Args:
            k (Any): The element to search for.

        Returns:
            Any: The element k if found, otherwise None.
        """
        if self.root:
            n = self.root.subtree_find(k)
            if n:
                return n.item

    def find_next(self, k):
        """
        Find the smallest element that is greater than k.

        Args:
            k (Any): The element for which the successor is to be found.

        Returns:
            Any: The next element greater than k, if exists.
        """
        if self.root:
            n = self.root.subtree_find_next(k)
            if n:
                return n.item

    def find_prev(self, k):
        """
        Find the largest element that is smaller than k.

        Args:
            k (Any): The element for which the predecessor is to be found.

        Returns:
            Any: The previous element smaller than k, if exists.
        """
        if self.root:
            n = self.root.subtree_find_prev(k)
            if n:
                return n.item

    def insert(self, x):
        """
        Insert a new element x into the tree.

        Args:
            x (Any): The element to insert into the tree.

        Returns:
            bool: True if new node was added, False if overwrite.
        """
        new_node = BSTNode(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None:
                # item was swapped, because x.key existed already
                return False
        else:
            self.root = new_node
        self.size += 1

    def delete(self, k):
        """
        Delete the element with value k from the tree.

        Args:
            k (Any): The element to delete from the tree.

        Returns:
            Any: The deleted element if found and deleted, otherwise None.
        """
        if not self.root:
            raise ValueError("Tree is empty, cannot delete")
        node = self.root.subtree_find(k)
        if not node:
            raise ValueError(f"No item for key={k}")
        removed = node.subtree_delete()
        if removed.parent is None:
            self.root = None
        self.size -= 1
        return removed.item


if __name__ == "__main__":
    seq = [37, 13, 49, 12, 39, 11]
    b = construct_binary_tree(seq)
    print(b)
    b.root.subtree_delete()
    print(b)
