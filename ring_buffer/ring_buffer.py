# FIFO
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.front = 0

    def append(self, item): 
        if len(self.data) == self.capacity:
            # if list is full, replace the first in item with new item
            self.data[self.front] = item
            # if we replaced all items in list already, set front back to index 0, else add one to replace next oldest item 
            if self.front == self.capacity - 1:
                self.front = 0
            else:
                self.front += 1
        else:
            # append an element at the end of the buffer
            self.data.append(item)

    def get(self):
        return self.data