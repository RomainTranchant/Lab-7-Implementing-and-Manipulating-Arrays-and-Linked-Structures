# Romain Tranchant
# CIS 103
# Fundamentals of programing
# Instructor: MD Ali
# Lab 7 : Implementing and Manipulating Arrays and Linked Structures


# Node class represents a single node in the linked list
# Each node contains some data and a reference to the next node (or None if it's the last node)
class Node:
# Constructor for Node class, initializes data and the next reference
    def __init__(self, data, next=None):
# Store the actual data in the node
        self.data = data
# Reference to the next node (default is None)
        self.next = next

# LinkedList class manages the entire linked list
class LinkedList:
# Constructor for LinkedList class, initializes an empty list
    def __init__(self):
# The linked list starts with no nodes, so the head is None
        self.head = None

# Insert a node at the beginning of the linked list
    def insert_at_beginning(self, data):
# Create a new node with the given data and link it to the current head
        new_node = Node(data, self.head)
# The new node's next is the current head
        self.head = new_node

# Insert a node at the end of the linked list
    def insert_at_end(self, data):
# If the list is empty, set the head to the new node
        if not self.head:
# Create a new node and set it as the head
            self.head = Node(data)
        else:
# Start from the head of the list
            probe = self.head
# Traverse the list to find the last node (where next is None)
# Iterate through the list until the last node and move to the next node
            while probe.next:
                probe = probe.next
# After reaching the last node, create a new node and link it as the next of the last node
# Add the new node at the end
            probe.next = Node(data)

# Traverse the entire list and print the data of each node
    def traverse(self):
# Start from the head of the list
        probe = self.head
# Loop as long as there are more nodes
        while probe:
# Print the data of the current node
            print(probe.data)
# Move to the next node
            probe = probe.next

# Search for a node by its data value
    def search(self, target):
# Start from the head of the list
        probe = self.head
# Iterate through the list to find the target value
        while probe:
# Check if the current node's data matches the target
            if probe.data == target:
# Target found, return True
                return True
# Move to the next node
            probe = probe.next
# Target not found, return False
        return False

# Delete a node at a specified position in the list
    def delete_at_position(self, index):
# Check if the position to delete is the head (index 0)
        if index == 0:
# Ensure the list is not empty
            if self.head:
# Move the head pointer to the next node (remove the old head)
                self.head = self.head.next
        else:
# Start from the head
            probe = self.head
# Traverse the list to find the node just before the one to delete
# Iterate up to the node before the one we want to delete
            for i in range(index - 1):
# If the index is out of range, return early
                if probe is None:
# No further action is needed
                    return
# Move to the next node
                probe = probe.next
# Check if the node to be deleted exists
# Ensure that there is a node after the current node
            if probe and probe.next:
# Skip the node to be deleted by updating the next pointer of the current node
# Link the current node to the node after the one being deleted
                probe.next = probe.next.next

# Example usage of the LinkedList class
if __name__ == "__main__":
# Create a new linked list object
    test_linkedlist = LinkedList()

# Insert elements at the beginning and at the end
    test_linkedlist.insert_at_beginning(150)  # Insert 150 at the beginning of the list
    test_linkedlist.insert_at_beginning(100)  # Insert 100 at the beginning of the list
    test_linkedlist.insert_at_beginning(90)   # Insert 90 at the beginning of the list
    test_linkedlist.insert_at_end(200)        # Insert 200 at the end of the list
    test_linkedlist.insert_at_end(300)        # Insert 300 at the end of the list
    test_linkedlist.insert_at_end(400)        # Insert 400 at the end of the list

# Print out the linked list after all insertions
    print("Linked List after insertions:")
# Traverse the list and print each node's data
    test_linkedlist.traverse()

# Search for specific elements in the list
    print(f"Search for 20: {test_linkedlist.search(20)}")  # Search for 20 (not in the list)
    print(f"Search for 300: {test_linkedlist.search(300)}")  # Search for 300 (present in the list)

# Delete a node at a specific position
    test_linkedlist.delete_at_position(2)  # Delete the node at position 2 (third node, which is 150)
# Print the linked list again after the deletion
    print("Linked List after deletion at position 2 (third node):")
# Traverse the list again to show the updated state
    test_linkedlist.traverse()