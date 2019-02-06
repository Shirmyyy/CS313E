#  File: TestLinkedList.py

#  Description: Assignment14

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/3/2018

#  Date Last Modified: 11/5/2018

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # get number of links
  def get_num_links (self):
    if (self.first == None):
      return 0

    current=self.first
    cnt=1 #because the current is the first for now, cnt=1
    while True:
      if (current.next == None):
        return cnt
      else:
        current = current.next
        cnt+=1 #when the current moves on to the next one, cnt +1

  # add an item at the beginning of the list
  def insert_first (self, data):
    new_link = Link (data)

    new_link.next = self.first
    self.first = new_link

  # add an item at the end of a list
  def insert_last (self, data):
    new_link = Link (data)

    current = self.first
    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # add an item in an ordered list in ascending order
  def insert_in_order (self, data):
    current = self.first
    previous = self.first
    new_link=Link(data)

    if (current == None): #if the list is empty
      self.insert_first(data)
      return

    while (current.data < data):
      if (current.next == None):#if current moves to the last one
        current.next=new_link
        return
      else:
        previous=current
        current = current.next

    if (current == self.first):#if the data is smaller than the first
      new_link.next=self.first
      self.first = new_link
    else:
      previous.next=new_link
      new_link.next=current

    return current

  # search in an unordered list, return None if not found
  def find_unordered (self, data):
    current = self.first


    if (current == None):
      return

    while (current.data != data):
      if (current.next == None):
        return
      else:
        current = current.next

    return current

  # Search in an ordered list, return None if not found
  def find_ordered (self, data):
      current=self.first

      if current==None:
          return

      while current.data<data:#stop searching if data is larger than current.data
          if current.next==None:
              return
          else:
              current=current.next

      if current.data!=data: #if they are not the same
          return
      return current

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
     strng=''
     current = self.first
     if (current == None):
       return ''

     cnt=1
     while (current!=None):
        if cnt==10:
            strng+=str(current.data)+'\n'
            current = current.next
            cnt=1 #return to 1 if change line
        else:
            strng+=str(current.data)+'  '
            current = current.next
            cnt+=1

     return (strng)

  # Copy the contents of a list and return new list
  def copy_list (self):
    li=LinkedList()
    current=self.first
    li.insert_last(current.data)
    current=current.next
    if (current == None):
      return None

    while current!=None:
        li.insert_last(current.data)
        current=current.next

    return li


  # Reverse the contents of a list and return new list
  def reverse_list (self):
    li=LinkedList()
    current=self.first
    li.insert_first(current.data)
    current=current.next

    if (current == None):
      return None

    while (current != None):
      li.insert_first(current.data)
      current = current.next

   # li.insert_first(current.data)

    return li

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
    li=LinkedList()
    current=self.first

    if (current == None):
      return None

    while (current != None):
      li.insert_in_order(current.data)
      current = current.next

    return li

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first

    if (current == None):
      return True

    while (current.next != None):
        if (current.data <= current.next.data):
            current = current.next
        else:
            return False

    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self):
      if self.get_num_links() == 0:
          return True
      else:
          return False

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
    li=LinkedList()
    current1=self.first
    current2=other.first

    while(current1!=None):
        li.insert_in_order(current1.data)
        current1=current1.next
    while (current2!=None):
        li.insert_in_order(current2.data)
        current2=current2.next
    return li


  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    num1=self.get_num_links()
    num2=other.get_num_links()
    if num1!=num2: #if they don't have the same length
        return False
    current1=self.first
    current2=other.first
    if self.is_empty() and other.is_empty():
        return True
    while (current1!=None and current2!=None):
        if current1.data==current2.data:
            current1=current1.next
            current2=current2.next
        else:
            return False

    return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    li=LinkedList()
    current=self.first
    unique_list=[]#a list containing all distinct data
    if (current == None):
      return None

    while current!=None:
        if current.data not in unique_list:
            unique_list.append(current.data)
            li.insert_last(current.data)
            current=current.next
        else:
            current=current.next

    return li

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  testList = [0,1,2,3,4,7,2,82,6957,2351,-5]
  blank=LinkedList()
#-------------------------------------------------------------------------------------------------
  print('insert_first')
  lst = LinkedList()

  for item in testList:
      lst.insert_first(item)
  print(lst)
  print()
#-------------------------------------------------------------------------------------------------
  # Test method insert_last()
  print("insert_last")
  lst.insert_last(100)
  print(lst)
  print()

#-------------------------------------------------------------------------------------------------
  # Test method insert_in_order()
  print("insert_in_order")

  lst5=LinkedList()
  lst5.insert_in_order(10)
  lst5.insert_in_order(10)
  lst5.insert_in_order(8)
  lst5.insert_in_order(1)
  lst5.insert_in_order(9)
  lst5.insert_in_order(1000)
  print(lst5)
  print()
#-------------------------------------------------------------------------------------------------
  # Test method get_num_links()
  print("get_num_links")

  print(lst.get_num_links())
  print()

#-------------------------------------------------------------------------------------------------
  # Test method find_unordered()
  # Consider two cases - data is there, data is not there
  print("find_unordered")

  print(lst.find_unordered(1))
  print(lst.find_unordered(90))
  print()

#-------------------------------------------------------------------------------------------------
  # Test method find_ordered()
  # Consider two cases - data is there, data is not there
  print("find_ordered")
  lst7=LinkedList()
  lst7.insert_last(1)
  lst7.insert_last(3)
  lst7.insert_last(5)
  lst7.insert_last(6)
  lst7.insert_last(9)
  lst7.insert_last(19)
  print(lst7.find_ordered(5))
  print(lst7.find_ordered(91))
  print()

#-------------------------------------------------------------------------------------------------
  # Test method delete_link()
  # Consider two cases - data is there, data is not there
  print('delete_link')
  lst.delete_link(100)
  print(lst)
  lst.delete_link(10000)
  print(lst)
  print()

#-------------------------------------------------------------------------------------------------
  # Test method copy_list()
  print('copy_list')
  print(lst)
  lst_copy=lst.copy_list()
  print(lst_copy)
  print()

#-------------------------------------------------------------------------------------------------
  # Test method reverse_list()
  print('reverse_list')
  print(lst)
  print(lst.reverse_list())
  print()

#-------------------------------------------------------------------------------------------------
  # Test method sort_list()
  print('sort_list')
  print(lst)
  lst_sort=lst.sort_list()
  print(lst_sort)
  print()

#-------------------------------------------------------------------------------------------------
  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print('is_sorted')
  print(lst)
  print(lst.is_sorted())
  lst2=LinkedList()
  lst2.insert_first(2)
  lst2.insert_first(1)
  lst2.insert_first(3)
  lst2.insert_first(6)
  lst2.insert_first(3)
  print(lst2)
  print(lst2.is_sorted())
  print()

#-------------------------------------------------------------------------------------------------
  # Test method is_empty()
  print('is_empty')
  lst3=LinkedList()
  print(lst.is_empty())
  print(lst3.is_empty())
  print()

#-------------------------------------------------------------------------------------------------
  # Test method merge_list()
  print('merge_list')
  print(lst)
  print(lst2)
  lst4=lst.merge_list(lst2)
  print(lst4)
  print()

#-------------------------------------------------------------------------------------------------
  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print('is_equal')
  print(lst.is_equal(lst_copy))
  print(lst.is_equal(lst4))
  print()

#-------------------------------------------------------------------------------------------------
  # Test remove_duplicates()
  print('remove_duplicates')
  print(lst4)

  print(lst4.remove_duplicates())
  print()
if __name__ == "__main__":
  main()
