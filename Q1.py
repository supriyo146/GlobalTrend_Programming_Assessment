# Implement a Python class MaxHeap that supports the following operations: insert, delete, and get_max. Ensure the operations maintain the properties of a max-heap.



class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, element):
        if element in self.heap:
            index = self.heap.index(element)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(index)

    def get_max(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index, right_child_index = 2 * index + 1, 2 * index + 2
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
print("Max value:", heap.get_max())  
heap.delete(30)
print("Max value after deleting 30:", heap.get_max())  
