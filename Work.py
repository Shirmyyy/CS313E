#  File: Work.py

#  Description: Assignment8

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 10/6/2018

#  Date Last Modified: 10/6/2018


#function to find v
def find_v(n,k,hi,lo):
    mid = lo + (hi - lo)//2

#if he first writes mid lines of code, he can finish his task, then mid is v
    if work_enough(n,mid,k,1,mid)==1:
        return mid

#if he first writes mid lines of code, he cannot finish his task
    elif work_enough(n,mid,k,1,mid)==0:

        #if he first writes mid+1 lines of code, he can finish his task, then mid+1 is v
        if work_enough(n,mid+1,k,1,mid+1)==2:
            return mid+1

        #if he first writes mid+1 lines of code, he cannot finish his task, then look at the other half
        else:
            return find_v(n,k,hi,mid)

#if he first writes mid lines of code, he cannot finish his task
    elif work_enough(n,mid,k,1,mid)==2:

        #if he first writes mid-1 lines of code, he cannot finish his task, then mid is v
         if work_enough(n,mid-1,k,1,mid-1)==0:
            return mid

        #if he first writes mid-1 lines of code, he cannot finish his task, then look at the other half
         else:
            return find_v(n,k,mid,lo)


def work_enough(n,v,k,p,lines):
    # the recursion stop when v//k**p==0
    if v//k**p==0:

        #count the lines to see if he writes enough lines
        if n>lines:
            return 0
        elif n==lines:
            return 1
        elif n<lines:
            return 2
    else:
        return work_enough(n,v,k,p+1,lines+v//k**p)


def main():
    in_file = open("work.txt", 'r')
    count = in_file.readline()

    for i in range(0, int(count)):
        n,k = in_file.readline().strip().split(' ')
        n = int(n)
        k = int(k)
        if not ((1 <= n <= 106) and (2 <= k <= 10)):
            print('Invalid input')
        else:
            print(find_v(n,k,n,1))


main()
