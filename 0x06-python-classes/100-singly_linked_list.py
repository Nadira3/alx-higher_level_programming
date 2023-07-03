#!/usr/bin/python3

"""
    Node: defines a node of a singly linked list
"""


class Node:

    """
        Node: defines a node of singly linked list

        data: list value
        next_node: next node containing data
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


"""
    SinglyLinkedList: defines a singly linked list
"""


class SinglyLinkedList:

    """
        SinglyLinkedList: defines a singly linked list

    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        nodePtr = self.__head
        while nodePtr.next_node:
            print(nodePtr.data)
            nodePtr = nodePtr.next_node
        return str(nodePtr.data)

    def sorted_insert(self, data):
        newNode = Node(data)
        nodePtr = self.__head
        if not nodePtr:
            self.__head = newNode
        elif not nodePtr.next_node:
            nodePtr.next_node = newNode
        else:
            while nodePtr.next_node and nodePtr.next_node.data < data:
                nodePtr = nodePtr.next_node
            newNode.next_node = nodePtr.next_node
            nodePtr.next_node = newNode
