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
        # Delete the line below and write your code here
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
        # Delete the line below and write your code here
        

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        # Delete the line below and write your code here
        raise NotImplementedError("dequeue not implemented")


    def is_full(self) -> bool:
        """Returns True if full or False otherwise"""

        return (self.tail + 1) % self.size == self.head
    



    returnn self.head




if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    pass