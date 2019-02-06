#  File: Triangle.py

#  Description: Assignment 13

#  Student's Name: Shimin Zhang

#  Student's UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/1/2018

#  Date Last Modified: 11/2/2018

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force_helper (grid,num_lines,lo,sum_path,sum_list,co):
    hi=num_lines
    if lo==hi:
      sum_list.append(sum_path)
      return
    else:
        #either use the left one or the right one
       sum_path=sum_path+grid[lo][co]
       brute_force_helper(grid,num_lines,lo+1,sum_path,sum_list,co)
       brute_force_helper(grid,num_lines,lo+1,sum_path,sum_list,co+1)

def brute_force(grid):
    sum_list = []
    brute_force_helper(grid,len(grid),0,0,sum_list,0)
    return sum_list

# returns the greatest path sum using greedy approach
def greedy_helper (grid,num_lines,sum_path,co):
    # always choose the bigger one
    for lo in range(num_lines-1):
        if grid[lo+1][co]>grid[lo+1][co+1]:
            sum_path=sum_path+grid[lo+1][co]
        else:
            co=co+1
            sum_path=sum_path+grid[lo+1][co]
    return sum_path

def greedy(grid):
    return greedy_helper(grid,len(grid),grid[0][0],0)

# returns the greatest path sum and the new grid using dynamic programming
def divide_conquer_helper(grid,num_lines,down,row): #divide the triangle into two triangle using the tips
    if row==num_lines-2:
        return grid[row][down]+max(grid[row+1][down+1],grid[row+1][down])
    else:
        return grid[row][down]+max(divide_conquer_helper(grid,num_lines,down,row+1),divide_conquer_helper(grid,num_lines,down+1,row+1))

def divide_conquer(grid):
    return divide_conquer_helper(grid,len(grid),0,0)

# returns the greatest path sum using divide and conquer (recursive) approach
def dynamic_prog_helper (grid,num_lines,down,row):
    if row==0:
        return grid[0][0]
    else:
        #work from bottom to up
        for down in range(len(grid[row])-1):
            grid[row-1][down]=grid[row-1][down]+max(grid[row][down],grid[row][down+1])
        return dynamic_prog_helper (grid,num_lines,down,row-1)

def dynamic_prog(grid):
    return dynamic_prog_helper(grid,len(grid),0,len(grid)-1)

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  in_file = open('./triangle.txt', 'r')
  triangle = []
  num_lines= int(in_file.readline().strip())
  for lines in range(num_lines):
      line=in_file.readline().strip().split()
      for i in range(len(line)):
          line[i]=int(line[i])
      triangle.append(line)

  return num_lines, triangle

def main ():
 # read triangular grid from file
  num_lines, triangle=read_file()

  # output greatest path from exhaustive search
  brute_force(triangle)
  print("The greatest path sum through exhaustive search is " + str(max(brute_force(triangle))) + ".")
  # print time taken using exhaustive search
  times = timeit ('brute_force({})'.format(triangle), 'from __main__ import brute_force', number = 10)
  times = times / 10
  print('The time taken for exhaustive search is '+str(times) + " seconds.")
  print()

  # output greatest path from greedy approach
  print("The greatest path sum through greedy search is " + str(greedy(triangle)) + ".")
  # print time taken using greedy approach
  times = timeit ('greedy({})'.format(triangle), 'from __main__ import greedy', number = 10)
  times = times / 10
  print('The time taken for greedy approach is '+str(times) + " seconds.")
  print()

#read the file to get the triangle again, because the triangle was ruined in the greedy approach
  num_lines, triangle=read_file()
 # output greatest path from divide-and-conquer approach
  print("The greatest path sum through recursive search is " + str(divide_conquer(triangle)) + ".")
  # print time taken using divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(triangle), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  print('The time taken for recursive search is '+str(times) + " seconds.")
  print()

  # output greatest path from dynamic programming
  print('The greatest path sum through dynamic programming is '+ str(dynamic_prog(triangle))+'.')
  # print time taken using dynamic programming
  times = timeit ('dynamic_prog({})'.format(triangle), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  print('The time taken for dynamic programming is '+str(times) + " seconds.")

if __name__ == "__main__":
  main()
