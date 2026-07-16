"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self._data = [None] * size
        self.head = -1
        self.tail = 0

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.tail == -1:
            raise IndexError('queue is full')
        if self.head == -1:
            self.head = self.tail

        self._data[self.tail] = item
        next_tail = (self.tail + 1) % self.size
        if next_tail == self.head:
            self.tail = -1
        else: 
            self.tail = next_tail

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        if self.head == -1:
            raise IndexError('queue is empty; nothing to dequeue')
        if self.tail == -1:
            self.tail = self.head
        value = self._data[self.head]
        next_head = (self.head + 1 ) % self.size
        if next_head == self.tail:
            self.head = -1
        else: 
            self.head = next_head
        return value
            


    def is_full(self) -> bool:
        """Returns True if full or False otherwise"""
        return (self.tail + 1) % self.size == self.head


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    pass