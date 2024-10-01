"""
Class to implement a priority queue using a heap data structure.
"""

class PriorityQueue:
    def __init__(self, max_heap=True):
        """set max_heap to True to create a max heap, otherwise a min heap is created"""
        self.heap = []
        self.size = 0
        self.max_heap = max_heap
    
    def insert(self, value):
        """Inserts a value into the heap"""
        self.heap.append(value)
        self.size += 1
        # Heapify up the last elemented added
        self._heapify_up(self.size - 1)

    def pop(self):
        """Removes the top element from the heap"""
        if self.size == 0:
            return None
        top = self.heap[0]
        # Move the last element to the top
        self.heap[0] = self.heap[self.size - 1]
        # Pop the last element, since it is now at the top
        self.heap.pop()
        self.size -= 1
        # Heapify down the top element
        self._heapify_down(0)
        return top

    def peek(self):
        """Returns the top element of the heap"""
        return self.heap[0] if self.size > 0 else None
    
    def _compare(self, i, j):
        """Compares two elements in the heap"""
        if self.max_heap:
            return self.heap[i] > self.heap[j]
        return self.heap[i] < self.heap[j]
    
    def _heapify_up(self, index):
        """Heapifies the heap from the bottom to the top"""
        if index == 0:
            return
        parent = (index - 1) // 2
        if self._compare(index, parent):
            self._swap(index, parent)
            self._heapify_up(parent)
    
    def _heapify_down(self, index):
        """Heapifies the heap from the top to the bottom"""
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < self.size and self._compare(left, largest):
            largest = left
        if right < self.size and self._compare(right, largest):
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)