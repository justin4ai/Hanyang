# Practice 13. Sorting
import sys

MERGE_SORT = 'M';
QUICK_SORT = 'Q';

def readInput(line, size):
  words = line.split()
  assert(len(words) == size)
  arr = [int(word) for word in words]
  return arr

def merge_sort(A, left, right):

  if left < right:

    mid = (left + right) // 2

    merge_sort(A, left, mid)
    merge_sort(A, mid + 1, right)

    merge(A, left, mid, right)


def merge(A, left, mid, right):

  n1 = mid - left + 1
  n2 = right - mid

  L, R = [0] * n1, [0] * n2

  for i in range(0, n1):
    L[i] = A[left + i]

  for j in range(0, n2):
    R[j] = A[mid + j + 1]

  i, j, k = 0, 0, left

  while (i < n1) and (j < n2):

    if L[i] > R[j]: # In descending order

      A[k] = L[i]
      i += 1

    else:
      A[k] = R[j]
      j += 1

    k += 1

  # Copying extras
  while i < n1:

    A[k] = L[i]
    i, k = i + 1, k + 1

  # Copying extras
  while j < n2:
    
    A[k] = R[j]
    j, k = j + 1, k + 1


def quick_sort(array):

  if len(array) <= 1: return array

  pivot = array[0] # Just a random pivot

  leftArray = [x for x in array[1:] if x <= pivot] # Partitioned left array
  rightArray = [x for x in array[1:] if x > pivot] # Partitioned right array

  return quick_sort(rightArray) + [pivot] + quick_sort(leftArray) # In descending order


if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")

  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      words = lines[i].split()
      op = words[0]
      if len(words) != 2:
        raise Exception("Error: invalid input")
      size = int(words[1])
      i += 1
      arr = readInput(lines[i], size)
      if op == MERGE_SORT:
        if len(words) != 2:
          raise Exception("MERGE_SORT: invalid input")
        else:
          merge_sort(arr, 0, size - 1)
          outFile.write(' '.join(list(map(str, arr))) + "\n")
      elif op == QUICK_SORT:
        if len(words) != 2:
          raise Exception("QUICK_SORT: invalid input")
        else:
          #quick_sort(arr, 0, size - 1)
          arr = quick_sort(arr)
          outFile.write(' '.join(list(map(str, arr))) + "\n")
      else:
        raise Exception("Undefined operator")
      i += 1

