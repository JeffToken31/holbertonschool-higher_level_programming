#!/usr/bin/python3
"""
This module use a class to define a node of a singly-linked list
"""


class Node:
    """
    define a node list
    """
    @property
    def data(self):
        """
        Getter of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter of data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter of next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setting next node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """
        Instantion of node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """
    Define a Singly Linked List containing the classes Node
    """
    def __init__(self):
        """
        Instantation of linked list
        """
        self.__head = None

    def __str__(self):
        """
        Prints list of node separate by a new line
        """
        new_str = ""
        current = self.__head
        while current:
            new_str += str(current.data)
            if current.next_node is not None:
                new_str += "\n"
            current = current.next_node
        return new_str

    def sorted_insert(self, value):
        """
        Insert a new node in position sorted in the list
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            current = self.__head
            while (
                current.next_node is not None
                and current.next_node.data < value
            ):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
