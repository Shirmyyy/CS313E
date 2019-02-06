#  File: TestBinaryTree.py

#  Description: Assignment17

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/15/2018

#  Date Last Modified: 11/16/2018

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self, nums):
    self.root = None

    #create the tree
    for i in nums:
      self.insert(i)

  def insert (self, ch):
    new_node = Node (ch)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ch < current.data):
            current = current.lchild
        elif (ch >= current.data):
            current = current.rchild
        else:
            return

      #insert as the leaf
      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  #get all the nodes in the tree into a list
  def in_order (self, aNode, lst):
    if aNode==None:
      return
    if (aNode != None):
      self.in_order (aNode.lchild,lst)
      lst.append(aNode.data)
      self.in_order (aNode.rchild,lst)

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    if self.root==pNode==None:
        return True
    lst1=[]
    lst2=[]
    self.in_order(self.root,lst1)
    self.in_order(pNode,lst2)
    if len(lst1)!=len(lst2): #if the length does not match, return false
        return False
    for i in range(len(lst1)):
        if lst1[i]!=lst2[i]:
            return False
    return True

  # Prints out all nodes at the given level
  def print_level_helper (self, level, aNode,cur_level,lst):
    if aNode==None:
        return

    if level>self.get_height():
        print('Invalid level')
        return
    if (aNode != None):
      self.print_level_helper (level,aNode.lchild,cur_level+1,lst)
      if cur_level==level: #append all the nodes that has a level equal to the given level
          lst.append(aNode.data)
      self.print_level_helper (level,aNode.rchild,cur_level+1,lst)

  def print_level(self,level):
     lst=[]
     self.print_level_helper(level,self.root,1,lst)
     for i in lst:
         print(i,end=' ')
     print()

  # Returns the height of the tree
  def get_height_helper (self,aNode,height,lst):
    if aNode==None:
        lst.append(height-1)#append all the heights when reach a leaf node
    else:
        self.get_height_helper(aNode.lchild,height+1,lst)
        self.get_height_helper(aNode.rchild,height+1,lst)
    return max(lst)

  def get_height(self):
      lst=[]
      return self.get_height_helper(self.root,1,lst)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes_helper (self,aNode):
    if aNode==None:
        return 0
    left=[]
    right=[]
    #divide the tree into a left tree and a right tree
    self.in_order(aNode.lchild,left)
    self.in_order(aNode.rchild,right)
    return(len(left)+len(right)+1)

  def num_nodes(self):
    return self.num_nodes_helper(self.root)

  def get_balance(self,aNode):
    if aNode==None:
        return 0
    left=[]
    right=[]
    #divide the tree into a left tree and a right tree
    self.in_order(aNode.lchild,left)
    self.in_order(aNode.rchild,right)
    return(len(left)-len(right))

def main():
    # Create three trees - two are the same and the third is different
    a=[0,0,0,0,0]
    b=[0,0,0,0,0]
    c=[1,2,3,5,6]

    tree_a=Tree(a)
    tree_b=Tree(b)
    tree_c=Tree(c)

    # Test your method is_similar()
    print('is similar')
    print(tree_a.is_similar(tree_b.root))
    print(tree_a.is_similar(tree_c.root))
    print()

    # Print the various levels of two of the trees that are different
    print('numbers in the same level')
    tree_a.print_level(4)
    tree_c.print_level(2)
    print()

    # Get the height of the two trees that are different
    print('get height')
    print(tree_a.get_height())
    print(tree_c.get_height())
    print()

    # Get the total numbe of nodes a binary search tree
    print('nums of nodes')
    print(tree_a.num_nodes())
    print(tree_c.num_nodes())
    print()
main()
