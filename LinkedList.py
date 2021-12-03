# _____________ SINGLE LINKED LIST _______________ #

class Node:
    def __init__(self, data):
        self.item = data  # input to be given as data
        self.ref = None  # reference or link to the next node


class LinkedList:
    def __init__(self):
        self.start_node = None  # Start node none as initially linked list is empty

    def traverse_list(self):  # Traversing linked list
        if self.start_node is None:  # Check if list is empty or not
            print("No element present in list")
            return
        else:
            n = self.start_node  # If not empty initialize to n starting node
            while n is not None:  # till n reaches null
                print(n.item, " ")
                n = n.ref

    def insert_start(self, data):  # Insert element at start
        new_node = Node(data)  # Create an obj of class Node
        new_node.ref = self.start_node  # Give previous start node as reference to new node
        self.start_node = new_node  # Make new node as start node

    def insert_end(self, data):  # Insert element at end
        new_node = Node(data)  #
        if self.start_node is None:  # Check if list is not empty
            self.start_node = new_node  # If empty , new node by default will be start node
            return
        n = self.start_node
        while n.ref is not None:  # if not empty iterate till end
            n = n.ref
        n.ref = new_node  # give new node's reference to the last node

    def delete_start(self):  # Delete from start
        if self.start_node is None:
            print("No element present to delete")
            return
        self.start_node = self.start_node.ref

    def delete_end(self):
        if self.start_node is None:
            print("No element present to delete")
            return
        n = self.start_node
        while n.ref is not None:  # If not empty iterate till end
            n = n.ref
        n.ref = None  # Change reference of second last node
