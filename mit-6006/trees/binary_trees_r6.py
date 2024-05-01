"""This module implements a binary tree."""

from __future__ import annotations
from typing import Any, Optional


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
        self.left: Optional[BinaryNode] = None
        self.right: Optional[BinaryNode] = None
        self.parent: Optional[BinaryNode] = None

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
        else:
            predecessor = self.left.subtree_last()
            # walked right as far as possible -> predecessor.right == None
            predecessor.right = new
            new.parent = predecessor

    def subtree_insert_after(self, new: BinaryNode):
        if not self.right:
            self.right = new
            new.parent = self
        else:
            successor = self.right.subtree_first()
            successor.left = new
            new.parent = successor

    def is_leaf(self):
        return self.left is None and self.right is None

    def subtree_delete(self):
        if self.is_leaf() and self.parent:
            if self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.left:
            # predecessor is guaranteed to be down the tree in left subtree of self
            lower_node = self.predecessor()
        elif self.right:
            # successor is guaranteed to be down the tree in right subtree of self
            lower_node = self.successor()
        self.item, lower_node.item = lower_node.item, self.item
        lower_node.subtree_delete()

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
        self.root: Optional[BinaryNode] = None
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

    def render_tree(self) -> str:
        """
        Renders the binary tree as a string representation.

        Returns:
            str: The string representation of the binary tree.
        """
        if not self.root:
            return "<empty tree>"

        lines = []
        current_level = [self.root]

        while any(current_level):
            next_level = []
            line = ""

            for node in current_level:
                if node:
                    line += f" {node.item} "
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    line += "   "  # Placeholder for empty node

            lines.append(line)
            current_level = next_level
        # Join lines with newline characters
        return "\n".join(lines)


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

    def subtree_find_if_present(self, k) -> Optional[BSTNode]:
        # find node storing k else find predecessor
        if k == self.item.key:
            return self
        if k < self.item.key:
            subtree = self.left
        if k > self.item.key:
            subtree = self.right
        if subtree:
            subtree.subtree_find(k)
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


if __name__ == "__main__":
    seq = [37, 13, 49, 12, 39, 11]
    b = construct_binary_tree(seq)
    print(b)
