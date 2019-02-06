#  File: Boxes.py

#  Description: Assignment10

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 10/18/2018

#  Date Last Modified: 10/18/2018

#test if a box can nest in another box
def nest(list1,list2):
    return list1[0]<list2[0] and list1[1]<list2[1] and list1[2]<list2[2]

#if the subset is composed by nesting boxes
def fitted(subset):
    for i in range(0, len(subset) -1):
        if not nest(subset[i], subset[i + 1]):
            return False
    return True

def remove_short(fitted_subset):
    #find the maximum length of list in fitted_subset
    max_len=2
    for i in fitted_subset:
        if len(i)>max_len:
            max_len=len(i)

    #find the lists in fitted_subset that have a length equal to the maximum length, and append them into largest_subset
    largest_subset=[]
    for i in fitted_subset:
        if len(i)==max_len:
            largest_subset.append(i)

    return largest_subset

#find all subsets
def sub_set(box_list,b,lo,box_subset):
    hi=len(box_list)
    if (lo==hi):
        box_subset.append(b)
    else:
        c=b[:]
        b.append(box_list[lo])
        sub_set(box_list,b,lo+1,box_subset)
        sub_set(box_list,c,lo+1,box_subset)
    return box_subset

def main():
    #open file for reading
    in_file=open('./boxes.txt','r')

    # read the number of boxes
    line=in_file.readline()
    line=line.strip()
    num_boxes=int(line)

    #create an empty list of boxes
    box_list=[]

    #read the list of boxes from the file
    for i in range(num_boxes):
        line=in_file.readline()
        line=line.strip()
        box=line.split()
        for j in range(len(box)):
            box[j]=int(box[j])
        box.sort()
        box_list.append(box)
    #close the file
    in_file.close

    #sort the box list
    box_list.sort()

    #get all subsets of boxes
    b=[]
    box_subset=[]
    all_subset=sub_set(box_list,b,0,box_subset)

    #check if all the boxes in a given subset fit and append all the fitted subset in to a fitted_subset
    fitted_subset=[]
    for i in all_subset:
        if fitted(i):
            fitted_subset.append(i)

    #find the largest_subset
    largest_subset=remove_short(fitted_subset)

    #sort the largest subset
    largest_subset.sort()

    #print all the largest subset of boxes
    if len(largest_subset)>0:
        print('Largest Subset of Nesting Boxes')
        for i in largest_subset:
            for j in i:
                print(j)
            print('')
    else:
        print('No Nesting Boxes')

main()
