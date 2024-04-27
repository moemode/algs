from typing import Any, Optional


class DoublyLinkedListNode:
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

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = DoublyLinkedListNode(x)
        old_head = self.head
        if old_head:
            new_node.next = old_head
            old_head.prev = new_node
        self.head = new_node

    def insert_last(self, x):
        new_node = DoublyLinkedListNode(x)
        old_tail = self.tail
        if old_tail:
            new_node.prev = old_tail
            old_tail.next = new_node
        self.tail = new_node

    def delete_first(self):
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

    def remove(self, node1: DoublyLinkedListNode, node2: DoublyLinkedListNode):
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

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! #
        ###########################
        pass
