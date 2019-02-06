#  File: TopoSort.py

#  Description: Assignment 19

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 12/2/2018

#  Date Last Modified: 12/3/2018

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

  # get a copy of the list of vertices
  def getVertices (self):
    lst=[]
    for i in self.Vertices:
      lst.append(i.label)
    return lst

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

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def hasCycle(self):
    if self.toposort()==-1:
      return True
    return False

  def find_leaves(self,result):
    leaves=[]
    sub_result=[]
    #find the vertex that do not have any successor
    for i in range (len(self.Vertices)):
      for j in range (len(self.Vertices)):
        if self.adjMat[i][j]>0:
          break
        elif j==len(self.Vertices)-1:
          leaves.append(i)

    #get all the leaves in a list and sort
    for i in leaves:
      sub_result.append(self.Vertices[i].label)
    sub_result.sort()

    #insert the subresult to the front
    for i in reversed(sub_result):
      result.insert(0,i)
    return leaves

  def delete_leaves(self,result):
    leaves=self.find_leaves(result)
    #make a copy of the vertices label before it getting ruined
    vertices_label_copy=[]
    for i in self.Vertices:
      vertices_label_copy.append(i.label)

    #delete all the leaves
    for i in leaves:
      self.deleteVertex(vertices_label_copy[i])

  def toposort(self):
    result=[] #a list that store the result

    #when there is vertex in the graph
    while len(self.Vertices)>0:
      len_before=len(self.Vertices) #get the number of vertices before deleting leaves
      self.delete_leaves(result)
      len_after=len(self.Vertices)  #get the number of vertices after deleting leaves
      if len_before==len_after:  #if we cannot delete any leaves from the graph, there must be a cycle inside of the graph
        return -1

    #the graph was ruined, rebuild the graph

    ########################################################################
    #  open file for reading
    inFile = open ("./topo.txt", "r")
    # read the Vertices
    numVertices = int ((inFile.readline()).strip())
    cities_list=[]
    for i in range (numVertices):
      city = (inFile.readline()).strip()
      self.addVertex (city)
      cities_list.append(city)
    # read the edges
    numEdges = int ((inFile.readline()).strip())
    for i in range (numEdges):
      edge = (inFile.readline()).strip()
      edge = edge.split()
      start = cities_list.index(edge[0])
      finish =cities_list.index(edge[1])
      weight = 1
      self.addDirectedEdge (start, finish, weight)
    inFile.close()
    #######################################################################

    return result

  def toposort2 (self):
    result=Stack()
    lst=[]
    for i in reversed(self.Vertices): #pick a starting point
        if not i.visited: #dfs this point
            self.dfs_toposort(self.Vertices.index(i),result)
    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    for i in range(len(result.stack)):
      lst.append(result.pop())
    return lst

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
  inFile = open ("./topo.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())

  cities_list=[]
  for i in range (numVertices):
    city = (inFile.readline()).strip()
    cities.addVertex (city)
    cities_list.append(city)


  # read the edges
  numEdges = int ((inFile.readline()).strip())

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    edge = edge.split()
    start = cities_list.index(edge[0])
    finish =cities_list.index(edge[1])
    weight = 1

    cities.addDirectedEdge (start, finish, weight)

  inFile.close()

  # test if a directed graph has a cycle
  if not (cities.hasCycle()):
    print(cities.toposort())

main()
