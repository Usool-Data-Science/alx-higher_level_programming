#!/usr/bin/python3
"""Contains 2 objects (Node, next_node).
    It is a simple implementation of a singly
    linked list. Where the next_node is either
    NULL or pointing to another instance of Node.
"""


class Node(object):
    """A blueprint for a Node object with data
        and next_node attributes.
    """
    def __init__(self, data, next_node=None):
        """Initialize the Node with data and next_node.

            Args:
                data (int): An integer attribute.
                next_node (Node/NULL): A new node or end.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Protect the data attribute by making it a
            private attribute.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data attribute to accept only integer
            entries otherwise raise a TypeError.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Protect the next_node attribute by makiing it
            a private attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Ensure next_node is either None or an instance
            of Node class; otherwise raise TypeError.
        """
        if ((value is None) or (isinstance(value, Node))):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList(Node):
    """A SinglyLinkedList that points to another node
        or just a None to indicate the end of the list.
    """
    def __init__(self):
        """Initialize the singlyLinkedList.
            Attr:
                head (Node/None): The head of the list.
        """
        self.__head = None
        # __head is now renamed as SinglyLinkedList__head

    def __str__(self):
        """Make the SinglyLinkedList printable.
            Create an emptly string and attach the value
            from each node to the string. The result it for
            printing.
        """
        result = ""
        # Call the value of the head using name mangling
        my_node = self._SinglyLinkedList__head
        # Iterate over all the nodes and attach their values
        while my_node:
            result += str(my_node.data) + "\n"
            # Shift to the next node
            my_node = my_node.next_node

        return result

    def sorted_insert(self, value):
        """Make a new Node for value, with next being None.
            If Head is None, set it to our new node;
            else if data of head is greater than new value:
                make new node point to head.
            For this scenario, we should have adopted the
            try/except/finally approach but we considered
            using the if/else approach instead.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        else:
            new_node = Node(value, None)
            # If the head is None or its data is >= new value
            if ((self.__head is None) or
                    self.__head.data >= value):
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                # Find the end of the linkedlist
                current_node = self.__head
                while ((current_node.next_node is not None) and
                        current_node.next_node.data < value):
                    current_node = current_node.next_node
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
