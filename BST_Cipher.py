#  File: BST_Cipher.py

#  Description: assignment16

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/11/2018

#  Date Last Modified: 11/11/2018

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      self.root = None

      encrypt_str=encrypt_str.lower()
      for i in encrypt_str:
          if i.isalpha() or i==' ':
            self.insert(i)
          else:
              continue

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
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
        elif (ch > current.data):
            current = current.rchild
        else:
            return

      #insert as the leaf
      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node


  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    current = self.root
    strng=''
    if current.data==ch:
        strng+='*' #if the ch = the root
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        current = current.lchild
        strng+='<'
      else:
        current = current.rchild
        strng+='>'

    return strng

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current=self.root
    if st=='*':
        return current.data
    elif st=='': #if this is a blank string
        return ''
    for i in st:
        if i == '<':
            current=current.lchild
        elif i=='>':
            current=current.rchild
    if current==None:
        return ''
    return current.data


  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    strng=''
    st=st.lower()
    #put a ! bewteen words but not after the final word or the string only have one word
    for i in range(len(st)):
        if st[i].isalpha() or st[i]==' ':
            strng+=self.search(st[i])
            strng+='!'
        else:
            continue

    return strng[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    strng=''
    st=st.strip().split('!')#the ! split different words
    for i in st:
        if i =='<'or'>'or'*':
            strng+=self.traverse(i)
    return strng


def main():
    encrypt_str=input('Enter encryption key: ')
    tree1=Tree(encrypt_str)
    print()
    st_encrypt=input('Enter string to be encrypted:')
    print('Encrypted string: '+ tree1.encrypt(st_encrypt))
    print()
    st_decrypt=input('Enter string to be decrypted:')
    print('Decrypted string: '+ tree1.decrypt(st_decrypt))

main()
