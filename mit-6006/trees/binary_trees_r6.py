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
