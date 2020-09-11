class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # return none if its empty
        if not node:
            return None
        # if node has no next, then we have a single element in our list
        elif not node.get_next():
            return node

        # Initializing values
        prev = None # initially points to None
        curr = node # points at the first element
        nex = curr.get_next() # points at the second element

        # Iterate through the linked list until current is None
        while curr:
            # reversing the link
            curr.set_next(prev)  

            # moving to next node      
            prev = curr
            curr = nex
            if nex:
                nex = nex.get_next()

        # Once the current becomes None, set the head pointer to the previous node
        self.head = prev
