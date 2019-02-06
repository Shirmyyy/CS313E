#  File: EvenMagicSquare.py

#  Description: Assignment11

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 10/22/2018

#  Date Last Modified: 10/23/2018

import sys

#the permute function
def permute (a, lo,num,magic_list):
  hi = len(a)
  #when the permutation reach the end of the list, transform the list into a 2-d list
  if (lo == hi):
    magic_square = []
    for k in range(4):
        magic_square += [[0] * 4]
    count=0
    for i in range (4):
        magic_square[i][0],magic_square[i][1],magic_square[i][2],magic_square[i][3]=a[0+count],a[1+count],a[2+count],a[3+count]
        count=count+4
    #check if the square is a magic square.If yes, append this magic square into a list
    if check_square(magic_square,4):
        magic_list.append(magic_square)
        #when we got enough number of magic squares, we print those magic squares
        if len(magic_list)==num:
            for i in range(len(magic_list)):
                print_square(magic_list[i])
            sys.exit(0)

  #if not reach the end, use the permutation function
  else:
    for i in range (lo, hi):
          a[lo], a[i] = a[i], a[lo]
          #optimization of the permutation function
          if (sum(a[:4])!=34 and lo==3) or (sum(a[4:8])!=34 and lo==7) or (sum(a[8:12])!=34 and lo==11) or (sum(a[12:16])!=34 and lo==15):
              a[lo], a[i] = a[i], a[lo]
              continue
          else:
             permute (a, lo + 1,num, magic_list)
             a[lo], a[i] = a[i], a[lo]

def print_square ( magic_square,n=4 ):

    #find the length of the maximum value
    max=magic_square[0][0]
    for i in range (n):
        for j in range (n-1):
            if max<magic_square[i][j+1]:
                max=magic_square[i][j+1]
    maxLen=len(str(max))

    #format the square
    for i in range (n):
        strng = ""
        for j in range(n):
            numOfSpace= maxLen - len(str(magic_square[i][j]))
            strng = strng+ (numOfSpace*" " +str(magic_square[i][j])+" "*2)
        print(strng)
    print('')


def check_square ( magic_square, n ):
    sum=int(n * (n*n + 1) / 2)

# rows
    for i in range(n):
        total=0
        for j in range(n):
            total += magic_square[i][j]
        if total!=sum:
           # print("This is not a magic square")
            return False


#colomns
    for i in range(n):
        total = 0
        for j in range(n):
            total += magic_square[j][i]
        if total != sum:
          #  print("This is not a magic square")
            return False


#diagonal from left to right
    total=0
    for i in range(n):
        total += magic_square[i][i]
    if total!=sum:
      #  print("This is not a magic square")
      return False

# diagonal from right to left
    total = 0
    a=0
    for i in range(n-1,-1,-1):
        total += magic_square[a][i]
        a+=1
    if total!=sum:
       # print("This is not a magic square")
        return False

    return True

def main():

    while True:
      num =int(input("Enter number of magic squares (1 - 10): "))
      if (num<1 or num>10):
          print("Your input is invalid")
          continue
      else:
          integers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
          magic_list=[]
          permute(integers,0,num,magic_list)


main()
