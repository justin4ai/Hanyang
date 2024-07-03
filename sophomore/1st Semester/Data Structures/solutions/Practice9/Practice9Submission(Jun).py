# Practice 9. Max Heap
import sys
INSERT = 'I'
DELETE = 'D'
MAXIMUM = 'M'
MAX_CAPACITY = 1000
INT_MIN = -sys.maxsize

class MaxHeap:
  def __init__(self, num=MAX_CAPACITY):
    self.elements = [0] * num
    self.count = 0 # the number of elements (not an index for the last element)
    self.capacity = num

  # Given the index i of element, return the index of that element's parent in the heap
  def parent(self, i):
    return (i - 1) // 2
  
  # Given the index i of element, return the index of that element's left child in the heap
  def left(self, i):
    return 2 * i + 1
  
  # Given the index i of element, return the index of that element's right child in the heap
  def right(Self, i):
    return 2 * i + 2

  # Insert a given element elem into the heap
  # If the insertion fails, immediately terminate the program with the error message.
  def insertElement(self, elem):

    if self.count >= self.capacity: raise Exception("Heap is already full!")

    if self.count == 0:
      self.elements[0] = elem
      self.count += 1
      return

    self.elements[self.count] = elem
    self.count += 1
    idx = self.count - 1 # Starts from the last node

    while ((idx > 0) and (self.elements[self.parent(idx)] < self.elements[idx])):
      self.elements[self.parent(idx)], self.elements[idx] = self.elements[idx], self.elements[self.parent(idx)] # Swapping
      idx = self.parent(idx)

  # Return the maximum of the heap if it exists
  # Otherwise, terminate program with an error
  def maximum(self):
    if self.count == 0:
      raise Exception("Heap is empty. There's not maximum.")

    return self.elements[0]

  def maxHeapify(self, i): # Newly added method for deletion
      left = self.left(i)
      right = self.right(i)
      largest = i
      if ((left < self.count) and (self.elements[left] > self.elements[largest])):
          largest = left
      if ((right < self.count) and (self.elements[right] > self.elements[largest])):
          largest = right
      if largest != i:
          self.elements[i], self.elements[largest] = self.elements[largest], self.elements[i]
          self.maxHeapify(largest)

  # Delete the maximum from the heap and return the maximum
  # If deletion fails, terminate program with an error
  def deleteMaximum(self):
    if self.count == 0: raise Exception("Heap is Already empty; You cannot delete anything.")

    maximum = self.elements[0]
    #print(f"maximum : {maximum}, count : {self.count}")
    self.elements[0] = self.elements[self.count - 1]
    self.elements[self.count - 1] = 0
    self.maxHeapify(0)
    self.count -= 1
    return maximum


if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  h = MaxHeap()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == INSERT:
        if len(words) != 2:
          raise Exception("INSERT: invalid input")
        i = int(words[1])
        h.insertElement(i)
        # If the insertion succeeds, write every element in the array into output file.
        outFile.write( ' '.join([str(ele) for ele in h.elements[:h.count]]) + '\n')
      elif op == DELETE:
        h.deleteMaximum()
        # If the deletion succeeds, write every element in the array into output file.
        outFile.write(' '.join([str(ele) for ele in h.elements[:h.count]]) + '\n')
      elif op == MAXIMUM:
        h.maximum()
        # If getting the maximum succeeds, write the maximum into output file.
        outFile.write(str(h.maximum()) + '\n')
      else:
        raise Exception("Undefined operator")
        

