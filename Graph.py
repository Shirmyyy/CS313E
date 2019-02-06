#  File: Graph.py

#  Description: Assignment18

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/29/2018

#  Date Last Modified: 11/29/2018
import sys
class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):

    if self.hasVertex(fromVertexLabel) and self.hasVertex(toVertexLabel):
        start=self.getIndex(fromVertexLabel)
        finish=self.getIndex(toVertexLabel)
        if self.adjMat[start][finish]==0:
            return -1
        return self.adjMat[start][finish]
    else:
        return -1

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    nVert=len (self.Vertices)
    neighbors=[]
    v=self.getIndex(vertexLabel)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0):
        neighbors.append(self.Vertices[i].label)
    return neighbors

  # get a copy of the list of vertices
  def getVertices (self):
    lst=[]
    for i in self.Vertices:
      lst.append(i.label)
    return lst

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    from_index=self.getIndex(fromVertexLabel)
    to_index=self.getIndex(toVertexLabel)
    self.adjMat[from_index][to_index] = 0
    self.adjMat[to_index][from_index] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
      v=self.getIndex(vertexLabel)
      nVert = len(self.Vertices)

    #delete from the vertex list
      self.Vertices.pop(v)

    # remove the column in the adjacency matrix for the Vertex
      for i in range (nVert):
        if v!=i:
            (self.adjMat[i]).pop(v)

      # remove the row in the adjacency matrix for the Vertex
      self.adjMat.pop(v)

  # add a Vertex with a given label to the graph
  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()

    # mark vertex v as visited and enqueue on the queue
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theQueue.enqueue (v)

   # vist other vertices according to depth
    while (not theQueue.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theQueue.queue[0])
      if (u == -1):
        u = theQueue.dequeue()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theQueue.enqueue(u)

    # the queue is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
  def hasCycle (self):

    #do a dfs on every vertex
    for i in range(len(self.Vertices)):
      theStack = Stack()

      (self.Vertices[i]).visited = True
      theStack.push (i)

      while (not theStack.isEmpty()):
        u = self.getAdjUnvisitedVertex (theStack.peek())
        #if the dfs runs back to the starting point, there is a cycle
        if i in self.getNeighbors(u):
          return True
        if (u == -1):
          u = theStack.pop()
        else:
          (self.Vertices[u]).visited = True
          theStack.push(u)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return False

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    result=Stack()
    for i in reversed(self.Vertices):
        if not i.visited:
            self.dfs_toposort(self.Vertices.index(i),result)
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return result

  def dfs_toposort (self, v,result):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        result.push(self.Vertices[theStack.peek()].label)
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        theStack.push(u)


def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())

  global Edge_list
  Edge_list = []
  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    Edge_list.append([start,finish,weight])# all index, not edge object
    Edge_list.sort(key = lambda column: (column[2])) # for spanning tree
    cities.addDirectedEdge (start, finish, weight)

  global nVert
  nVert = len (cities.Vertices)
  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()

  #read two cities for deleting the edges
  edges_cities=(inFile.readline()).strip()
  start,finish=edges_cities.split(' ')

  #read the vertex that needs to be removed
  delete_vertex=(inFile.readline()).strip()

  # close file
  inFile.close()

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)

  # do depth first search
  print ("Depth First Search")
  cities.dfs (startIndex)
  print()

  # test breadth first search
  print ("Breadth First Search")
  cities.bfs (startIndex)
  print()



  # test deletion of an edge
  print('Deletion of an edge')
  cities.deleteEdge(start,finish)

  print ("\nAdjacency Matric")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # test deletion of a vertex
  print('Deletion of a vertex')
  print()
  cities.deleteVertex(delete_vertex)

  print('List of Vertices')
  for i in cities.Vertices:
      print (i)

  print ("\nAdjacency Matric")
  for i in range (len(cities.Vertices)):
    for j in range (len(cities.Vertices)):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()


main()
