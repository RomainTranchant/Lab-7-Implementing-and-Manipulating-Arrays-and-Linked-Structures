# Romain Tranchant
# CIS 103
# Fundamentals of programing
# Instructor: MD Ali
# Lab 7 : Implementing and Manipulating Arrays and Linked Structures

# Define a custom class called Array
class Array:
# Constructor (__init__) initializes the array with a given capacity and fill_value.
# If no fill_value is provided, it will default to None.
    def __init__(self, capacity, fill_value=None):
# Create a list of 'capacity' size, filled with 'fill_value' (default is None)
        self.items = [fill_value] * capacity

# Method to return the current size (number of elements) in the array.
    def __len__(self):
# Return the length of the internal list (self.items)
        return len(self.items)

# Method to return a string representation of the array.
    def __str__(self):
# Convert the internal list to a string and return it for easy printing.
        return str(self.items)

# Method to retrieve an item from the array at a specific index.
    def __getitem__(self, index):
# Return the item at the given index from the internal list.
        return self.items[index]

# Method to assign a value to an item at a specific index.
    def __setitem__(self, index, value):
# Set the item at the given index to the new value.
        self.items[index] = value

# Method to insert a new element at a specified index in the array.
    def insert(self, index, value):
# Check if the index is valid (within bounds).
        if index < 0 or index > len(self.items):
# Raise an error if the index is out of bounds.
            raise IndexError("Index out of bounds")
# Perform the insertion by slicing the list, inserting the value, and then joining the list.
        self.items = self.items[:index] + [value] + self.items[index:]

# Method to delete an element at a specified index in the array.
    def delete(self, index):
# Check if the index is valid (within bounds).
        if index < 0 or index >= len(self.items):
# Raise an error if the index is out of bounds.
            raise IndexError("Index out of bounds")
# Perform the deletion by slicing the list and excluding the element at 'index'.
        self.items = self.items[:index] + self.items[index + 1:]

# Method to increase the size of the array to a new capacity.
    def increase_size(self, new_capacity):
# Ensure that the new capacity is greater than the current size of the array.
        if new_capacity <= len(self.items):
# Raise an error if the new capacity is not larger than the current capacity.
            raise ValueError("New capacity must be greater than current capacity")
# Increase the array size by appending zero values to the internal list.
        self.items += [0] * (new_capacity - len(self.items))

# Method to decrease the size of the array to a new capacity.
    def decrease_size(self, new_capacity):
# Ensure that the new capacity is valid (greater than or equal to 0 and not larger than the current size).
        if new_capacity < 0 or new_capacity > len(self.items):
# Raise an error if the new capacity is not within valid bounds.
            raise ValueError("New capacity must be within current size bounds")
# Decrease the size by truncating the list to the new capacity.
        self.items = self.items[:new_capacity]

# The following section is for testing the Array class.


# Check if this script is being run as the main module.
if __name__ == "__main__":
# Initialize an Array object with a capacity of 8, filled with zeros.
    array = Array(8, fill_value=0)
# Print the initial state of the array.
    print(f"The initial array: {array}")

# Test the insertion method: insert 10 at index 3.
    array.insert(3, 10)  # Insert 10 at index 3
# Print the array after the insertion.
    print(f"Array after inserting 10 at index 3: {array}")

# Test the deletion method: delete the element at index 2.
    array.delete(2)  # Delete element at index 2
# Print the array after the deletion.
    print(f"Array after deleting element at index 2: {array}")

# Test the increase_size method: increase the array size to 16.
    array.increase_size(16)  # Increase size to 16
# Print the array after increasing its size.
    print(f"Array after increasing size to 16: {array}")

# Test the decrease_size method: decrease the array size to 4.
    array.decrease_size(4)  # Decrease size to 4
# Print the array after decreasing its size.
    print(f"Array after decreasing size to 4: {array}")

# Print the final state of the array after all operations.
    print(f"The final array: {array}")


