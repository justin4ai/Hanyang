# Practice 10. Graph Representation
import sys
from collections import defaultdict, deque


CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
BFS = 'B'
DFS = 'D'
REACHABILITY = 'R'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'

tasks = [CONSTRUCT, IS_ADJACENT, GET_NEIGHBORS, BFS, DFS, REACHABILITY, TOPOLOGICAL_SORT, SHORTEST_PATH]

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

    self.size = max(self.size, max(u, v)) # Since the id starts from 0 and increases by 1, this is valid

  def isConnected(self, u, v):

    lineToWrite = f'{u} {v} T\n' if v in [tup[0] for tup in self.adjacencyList[u]] else f'{u} {v} F\n'
    outFile.write(lineToWrite)

  def getNeighbors(self, u):

    outFile.write(' '.join([str(tup[0]) for tup in self.adjacencyList[u]]) + '\n')

  def dfs(self, src):
    lineToWrite = ''
    myStack = [src]
    visited = [False for i in range(self.size)]

    while len(myStack) != 0 :
      vertex = myStack.pop()
      lineToWrite += f'{vertex} '

      if visited[vertex] == False:
        visited[vertex] = True

        for neighbor in [ tup[0] for tup in self.adjacencyList[vertex] ]:
          if visited[neighbor] == False:
            myStack.append(neighbor)

    outFile.write(lineToWrite + "\n")

  def bfs(self, src):
    lineToWrite = ''
    myQueue = deque([src])

    visited = [False for i in range(self.size)]
    visited[src] = True

    while len(myQueue) != 0 :
      vertex = myQueue.popleft()
      lineToWrite += f'{vertex} '


      if vertex in self.adjacencyList:
        for neighbor in [ tup[0] for tup in self.adjacencyList[vertex] ]:
          if visited[neighbor] == False:
            visited[neighbor] = True
            myQueue.append(neighbor)

    outFile.write(lineToWrite + "\n")

  def topologicalSort(self):

    inDegree = defaultdict(int)
    for id in range(self.size):
      inDegree[id]

    for node in self.adjacencyList:
      for neighbor in [ tup[0] for tup in self.adjacencyList[node] ]:
        inDegree[neighbor] += 1

    res = []
    myQueue = deque([vertex for vertex in self.adjacencyList if inDegree[vertex] == 0])


    while len(myQueue) != 0:
      vertex = myQueue.popleft()
      res.append(vertex)

      for neighbor in [ tup[0] for tup in self.adjacencyList[vertex] ]:
        inDegree[neighbor] -= 1
        if inDegree[neighbor] == 0:
          myQueue.append(neighbor)

    return res

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

          if words[0] in tasks: # If the task has been changed during construction
            raise Exception("Insufficient edges for construction")

          g.addEdge(int(words[0]), int(words[1]), int(words[2]))
        g.size += 1
        if lines[i+1].split()[0] not in tasks:
          raise Exception("Too much edges for construction")
        if g.size != n:
          print(f"Testing : g.size : {g.size}")
          raise Exception("Insufficient vertices for construction")

        for id in range(g.size):
          if id not in g.adjacencyList:
            g.adjacencyList[id] = set()

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
        g.dfs(int(src))
      elif op == BFS:
        src = words[1]
        g.bfs(int(src))
      elif op == TOPOLOGICAL_SORT:
        t = g.topologicalSort()
        if len(t) != g.size:
          raise ValueError("The given graph is not a DAG")

        outFile.write(' '.join(map(str, t)) + '\n')
      else:
        raise Exception("Undefined operator")
      i += 1
