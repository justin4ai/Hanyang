# Practices 6&7. Binary Search Tree Operations
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'
SEARCH = 'S'
INSERT = 'I'
DELETE = 'D'
INORDER = 'N'
PREORDER = 'R'
POSTORDER = 'O'

# Node implementation
class TreeNode:
  def __init__(self, k, l=None, r=None):
    self.key = k
    self.left = l
    self.right = r

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # Return True if tree is empty; False otherwise
  def isEmpty(self):
    return self.root == None

  # Given a sequence arr of integers, start index l, the end index r, 
  # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
  # Return the root node of the tree
  def arrayToBST(self, arr, l, r):
    if arr != list(sorted(arr)): raise Exception("The given array is not sorted.")

    def med(arr):
      return (len(arr) - 1) // 2

    self.root = TreeNode(arr[med(arr)])
    leftArr, rightArr = arr[:med(arr)], arr[med(arr) + 1:]

    def dfs(curNode, leftArr, rightArr):
      if leftArr != []:
        med_left = med(leftArr)
        curNode.left = TreeNode(leftArr[med_left])
        dfs(curNode.left, leftArr[:med_left], leftArr[med_left + 1:])

      if rightArr != []:
        med_right = med(rightArr)
        curNode.right = TreeNode(rightArr[med_right])
        dfs(curNode.right, rightArr[:med_right], rightArr[med_right + 1:])

    dfs(self.root, leftArr, rightArr)
    return self.root

  def findMin(self): # Time complexity : O(n)

    cursor = self.root

    if cursor == None: return None

    while cursor.left != None:
      cursor = cursor.left

    return cursor

  # Return the node with the maximum value
  def findMax(self): # Time complexity : O(n)

    cursor = self.root

    if cursor == None: return None

    while cursor.right != None:
      cursor = cursor.right

    return cursor

  def _getHeight(self, curr):
    if not curr:
      return 0
    return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

  def _printSpaces(self, n, curr):
    for i in range(int(n)):
      print("  ", end="")
    if not curr:
      print(" ", end="")
    else:
      print(str(curr.key), end="")

  def printTree(self):
    if not self.root:
      return 
    q = deque()
    q.append(self.root)
    temp = deque()
    cnt = 0
    height = self._getHeight(self.root) - 1
    nMaxNodes = 2**(height + 1) - 1
    while cnt <= height:
      curr = q.popleft()
      if len(temp) == 0:
        self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
      else:
        self._printSpaces(nMaxNodes / (2**cnt), curr)
      if not curr:
        temp.append(None)
        temp.append(None)
      else:
        temp.append(curr.left)
        temp.append(curr.right)
      if len(q) == 0:
        print("\n")
        q = temp
        temp = deque()
        cnt += 1

  # Given a query, search for the node whose key is equal to query.
  # If the node exists, return the key
  # Otherwise, return nullptr  
  def search(self, query): # Time complexity : O(n)

    def searchWithPointer(p, q):
      if q == p.key: return p

      elif (q < p.key) and (p.left != None):
        return searchWithPointer(p.left, q)

      elif (q > p.key) and (p.right != None):
        return searchWithPointer(p.right, q)

      return p

    return searchWithPointer(self.root,query)

  # Given an output file, write the keys of all the nodes 
  # visited in inorder traversal
  def writeInorder(self, outFile): # Time complexity : O(n)
    self.lineToWrite = ""
    self.container = []

    def Inorder(node):

      if node == None: return
      Inorder(node.left)
      self.lineToWrite += f'{node.key} '
      Inorder(node.right)

    print(self.lineToWrite)
    Inorder(self.root)
    outFile.write(self.lineToWrite + "\n")

  # Given an output file, write the keys of all the nodes 
  # visited in preorder traversal
  def writePreorder(self, outFile): # Time complexity : O(n)
    self.lineToWrite = ""
    self.container = []

    def Preorder(node):

      if node == None: return
      self.lineToWrite += f'{node.key} '
      Preorder(node.left)
      Preorder(node.right)

    print(self.lineToWrite)
    Preorder(self.root)
    outFile.write(self.lineToWrite + "\n")


  
  # Given an output file, write the keys of all the nodes 
  # visited in postorder traversal
  def writePostorder(self, outFile): # Time complexity : O(n)
    self.lineToWrite = ""
    self.container = []

    def Postorder(node):
      if node == None: return

      Postorder(node.left)
      Postorder(node.right)
      self.lineToWrite += f'{node.key} '

    print(self.lineToWrite)
    Postorder(self.root)
    outFile.write(self.lineToWrite + "\n")
  
  # If node with key k alreay exists in the tree, do nothing
  # Otherwise, insert new node with key k 
  def insertNode(self, k): # Time complexity : O(n)

    if self.root == None:
      self.root = TreeNode(k)
      return

    p = self.search(k)
    if k < p.key:
      p.left = TreeNode(k)
    elif k > p.key:
      p.right = TreeNode(k)

  def minimumPointer(self, root): # Added function

    cursor = root

    while cursor.left != None:
      cursor = cursor.left

    return cursor

  # If deletion fails, immediately terminate the program
  # Otherwise, delete the node with key k
  def deleteNode(self, k): # Time complexity : O(n)

    if self.root == None: raise Exception("Deletion failed because there's no node at all")

    parent, cursor = None, self.root

    while (cursor != None) and (cursor.key != k): # Search the node to be deleted
      parent = cursor

      cursor = cursor.left if k < cursor.key else cursor.right

    if cursor is None: # cursor == None means it went too deep since there's no target
      raise Exception("Deletion failed because there is no target node.")

    if (cursor.left == None) and (cursor.right == None): # 1) No children

      if cursor != self.root:
        if parent.left == cursor:
          parent.left = None
        else:
          parent.right = None

      else:
        self.root = None # This is also a deletion when
        return True      # it was a root node and a target at the same time

    elif (cursor.left) and (cursor.right): # Two children

      successor = self.minimumPointer(cursor.right)
      val = successor.key

      self.deleteNode(successor.key) # Recursive deletion for successors

      cursor.key = val


    else: # One child

      child = cursor.left if cursor.left else cursor.right

      if cursor != self.root:
        if cursor == parent.left:
          parent.left = child
        else:
          parent.right = child

      else:
        self.root = child

    return True

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  tree = BinarySearchTree()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == BUILD:
        data = [int(s) for s in words[1:]]
        tree.root = tree.arrayToBST(data, 0, len(data) - 1)
        if tree.root:
          outFile.write(BUILD + "\n")
          tree.printTree()
        else:
          raise Exception("BUILD: invalid input")
      elif op == FIND_MIN:
        found = tree.findMin()
        if not found:
          raise Exception("FindMin failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == FIND_MAX:
        found = tree.findMax()
        if not found:
          raise Exception("FindMax failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == SEARCH:
        if len(words) != 2:
          raise Exception("SEARCH: invalid input")
        k = int(words[1])
        if tree.search(k).key == k:
          outFile.write(str(k) + "\n")
        else:
          raise Exception("The given query does not exist in the tree.")

      elif op == INORDER:
        tree.writeInorder(outFile)
        pass
      elif op == PREORDER:
        tree.writePreorder(outFile)
      elif op == POSTORDER:
        tree.writePostorder(outFile)
      elif op == INSERT:
        if len(words) != 2:
          raise Exception("INSERT: invalid input")
        k = int(words[1])
        tree.insertNode(k)
        outFile.write(line)
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        k = int(words[1])

        if tree.deleteNode(k) == True:
          outFile.write(line)
        # else : None # no else case needed since it will
                    # have raised an exception already

      else:
        raise Exception("Undefined operator")
        
