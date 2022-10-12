#!/usr/bin/python3
""" Singly linked list module"""

class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Node instance initializer"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """Initializes SinglyLinkedList instances"""
        self.head = None

    def __str__(self):
        """Returns head"""
        s = ""
        node = self.head
        while node:
            s += str(node.data) + "\n"
            node = node.next_node
        return s[:-1]

    def sorted_insert(self, value):
        """A method to insert a node"""
        n = Node(value)
        if not self.head:
            self.head = n
            return

        if value < self.head.data:
            n.next_node = self.head
            self.head = n
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            n.next_node = node.next_node
        node.next_node = n 
