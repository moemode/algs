"""
DoublyLinkedListSeq Implementation.
"""

from __future__ import annotations
from typing import Any, Optional


class DoublyLinkedListNode:
    """
    Each node x of a doubly linked list maintains an x.prev pointer
    to the node preceeding it in the sequence,
    in addition to an x.next pointer to the node following it in the sequence.
    """

    def __init__(self, x: Any):
        self.item: Any = x
        self.prev: Optional[DoublyLinkedListNode] = None
        self.next: Optional[DoublyLinkedListNode] = None

    def later_node(self, i):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class DoublyLinkedListSeq:
    """
    A doubly linked list L maintains a pointer to L.tail,
    the last node in the sequence, in addition to L.head,
    the first node in the sequence.
    """

    def __init__(self):
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return "-".join([("(%s)" % x) for x in self])

    def __repr__(self):
        return "-".join([("(%s)" % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x: Any) -> None:
        """Inserts a new node with the given value at the beginning of the sequence.

        Args:
            x (Any): The value to be inserted.
        """
        new_node = DoublyLinkedListNode(x)
        old_head = self.head
        if old_head:
            new_node.next = old_head
            old_head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = self.head

    def insert_last(self, x) -> None:
        """Inserts a new node with the given value at the end of the doubly linked list.

        Args:
            x (Any): The value to be inserted.
        """
        new_node = DoublyLinkedListNode(x)
        old_tail = self.tail
        if old_tail:
            new_node.prev = old_tail
            old_tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = self.tail

    def delete_first(self) -> Any:
        """Remove and return the first item from the doubly linked list.

        Raises:
            IndexError: If the doubly linked list is empty.

        Returns:
            Any: The item that was removed from the doubly linked list.
        """
        if not self.head:
            raise IndexError()
        to_delete = self.head
        if self.head == self.tail:
            # one element
            self.head = None
            self.tail = None
        else:
            # at least two elements
            succ = to_delete.next
            succ.prev = None
            to_delete.next = None
            self.head = succ
        return to_delete.item

    def delete_last(self):
        """Remove and return the last item from the doubly linked list.

        Raises:
            IndexError: If the doubly linked list is empty.

        Returns:
            Any: The item that was removed from the doubly linked list.
        """
        if not self.tail:
            raise IndexError()
        to_delete = self.tail
        if self.head == self.tail:
            # one element
            self.head = None
            self.tail = None
        else:
            # at least two elements
            pre = to_delete.prev
            pre.next = None
            to_delete.prev = None
            self.tail = pre
        return to_delete.item

    def remove(
        self, node1: DoublyLinkedListNode, node2: DoublyLinkedListNode
    ) -> DoublyLinkedListSeq:
        """Given two nodes x1 and x2 from a doubly linked list L, where x1 occurs before x2,
          remove all nodes from x1 to x2 inclusive from L, and return them as a new doubly linked list.

        Args:
            node1 (DoublyLinkedListNode): The first node in the range to be removed.
            node2 (DoublyLinkedListNode): The last node in the range to be removed.

        Returns:
            DoublyLinkedListSeq: A new doubly linked list containing the removed nodes.
        """
        sublist = DoublyLinkedListSeq()
        pre = node1.prev
        post = node2.next
        if self.head == node1:
            self.head = post
        if self.tail == node2:
            self.tail = pre
        if pre:
            node1.prev = None
            pre.next = post
        if post:
            node2.next = None
            post.prev = pre
        sublist.head = node1
        sublist.tail = node2
        return sublist

    def splice(
        self, insert_after: DoublyLinkedListNode, other_list: DoublyLinkedListSeq
    ) -> None:
        """Splice list other_list into list self after node x.

        Given node x from a doubly linked list self and second doubly linked list other_list,
        this method splices list other_list into list self after node x. After the splice operation,
        self should contain all items previously in either list, and other_list should be empty.

        Args:
            insert_after (DoublyLinkedListNode): The node in self after which other_list should be spliced.
            other_list (DoublyLinkedListSeq): The second doubly linked list other_list to be spliced into self.
        """
        if not other_list.head:
            # other_list is empty
            return
        post = insert_after.next
        insert_after.next = other_list.head
        other_list.head.prev = insert_after
        if post:
            post.prev = other_list.tail
            other_list.tail.next = post
        else:
            # no post so tail of other_list is new tail of this list
            self.tail = other_list.tail
        other_list.head = None
        other_list.tail = None
