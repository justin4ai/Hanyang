# Practice 10. Graph Representation 
import sys
from collections import deque


CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
BFS = 'B'
DFS = 'D'
REACHABILITY = 'R'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'

class Graph:

  def __init__(self):
    self.adjacencyList = dict()
    self.size = 0

  def addEdge(self, u, v, weight):

    if u in self.adjacencyList :
      self.adjacencyList[u].update([(v, weight)])

    else :
      self.adjacencyList[u] = set()
      self.adjacencyList[u].update([(v, weight)])

  def isConnected(self, u, v):

    lineToWrite = f'{u} {v} T\n' if v in [tup[0] for tup in self.adjacencyList[u]] else f'{u} {v} F\n'
    outFile.write(lineToWrite)

  def getNeighbors(self, u):

    outFile.write(' '.join([str(tup[0]) for tup in self.adjacencyList[u]]) + '\n')

  def dfs(self, src):
    lineToWrite = ''
    myStack = [src]
    visited = [False for i in range(self.size)]

    while myStack != None :
      vertex = myStack.pop()
      lineToWrite += f'{vertex} '
      myStack[vertex] = True

      if vertex in self.adjacencyList:
        for neighbor in [ tup[0] for tup in self.adjacencyList[vertex] ]:
          if visited[neighbor] == False:
            myStack.append(neighbor)

    outFile.write(lineToWrite)

  def bfs(self, src):
    lineToWrite = ''
    myQueue = deque()
    myQueue.append(src)
    visited = [False for i in range(self.size)]

    while myQueue != None :
      vertex = myQueue.popleft()
      lineToWrite += f'{vertex} '
      myQueue[vertex] = True

      if vertex in self.adjacencyList:
        for neighbor in [ tup[0] for tup in self.adjacencyList[vertex] ]:
          if visited[neighbor] == False:
            myQueue.append(neighbor)

    outFile.write(lineToWrite)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")

  g = Graph()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      words = lines[i].split()
      op = words[0]
      if op == CONSTRUCT:
        if len(words) != 3:
          raise Exception("CONSTRUCT: invalid input")
        n, m = int(words[1]), int(words[2]) # n : number of vertices / m : number of edges
        cnt, data = m, []
        for j in range(cnt):
          i += 1
          words = lines[i].split()

          if words[0] in [CONSTRUCT, IS_ADJACENT, GET_NEIGHBORS, BFS, DFS, REACHABILITY, TOPOLOGICAL_SORT, SHORTEST_PATH]: # If the task has been changed during construction
            raise Exception("Insufficient edges for construction")

          g.addEdge(int(words[0]), int(words[1]), int(words[2]))
        if lines[i+1].split()[0] not in [CONSTRUCT, IS_ADJACENT, GET_NEIGHBORS, BFS, DFS, REACHABILITY, TOPOLOGICAL_SORT, SHORTEST_PATH]:
          print(lines[i+1].split()[0])
          print('**********')
          raise Exception("Too much edges for construction")
        if len(g.adjacencyList.keys()) != n:
          raise Exception("Insufficient vertices for construction")
      elif op == IS_ADJACENT:
        if len(words) != 3:
          raise Exception("IS_ADJACENT: invalid input")
        u, v = int(words[1]), int(words[2])
        g.isConnected(u, v)
      elif op == GET_NEIGHBORS:
        if len(words) != 2:
          raise Exception("GET_NEIGHBORS: invalid input")
        u = int(words[1])
        g.getNeighbors(u)

      elif op == DFS:
        src = words[1]
        g.DFS(src)
      elif op == BFS:
        src = words[1]
        g.BFS(src)
      elif op == TOPOLOGICAL_SORT:
        pass
      else:
        raise Exception("Undefined operator")
      i += 1
