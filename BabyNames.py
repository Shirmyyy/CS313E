#  File: BabyNames.py

#  Description: Assignment 3

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/12/2018

#  Date Last Modified: 9/14/2018

#To test if the list is ranked from large to small
def morePopular(lst):
    for i in range (len(lst)):
        if lst[i]==0:
            lst[i]=1001
    for i in range (len(lst)-1):
        if lst[i+1]>=lst[i]:
            return False
    return True

#To test if the list is ranked from small to large
def lessPopular(lst):
    for i in range (len(lst)):
        if lst[i]==0:
            lst[i]=1001
    for i in range (len(lst)-1):
        if lst[i+1]<=lst[i]:
            return False
    return True

#The list was ruined in the previous to functions. Now return the list to the original version
def backToOriginal(dict):
    for key in dict:
        lst = dict[key]
        for i in range(len(dict[key])):
            if lst[i] == 1001:
                lst[i] = 0



def main():
    nameFile = open('names.txt', 'r')
    babyNames = {}

#Put the names.txt into a dictionary
    try:
        for line in nameFile:
            name, d1900, d1910, d1920, d1930, d1940, d1950, d1960, d1970, d1980, d1990, d2000 = line.split(' ')
            rankings = [d1900, d1910, d1920, d1930, d1940, d1950, d1960, d1970, d1980, d1990, d2000]
            for i in range(len(rankings)):
                rankings[i] = int(rankings[i])

            babyNames[name] = rankings
    except IOError:
        print('Cannot open file.')
    finally:
        nameFile.close()

    while True:
        # Menu choices
        print('Options:')
        print('Enter 1 to search for names.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.')
        print(' ')

        try:
            choice = int(input('Enter choice: '))
            if 0<choice<7: #The user input should be within the menu choices

                # Option 1
                if choice == 1:
                    try:
                        name = input('Enter a name: ')
                        if name in babyNames:
                            print(' ')
                            print('The matches with their highest ranking decade are: ')
                            minNum=min(babyNames[name]) #Find the minimum ranking
                            idx=babyNames[name].index(minNum) #Find the index of the minimum ranking
                            year=1900+idx*10 #Convert the index to year
                            print(name+' '+str(year))

                        else:
                            print(' ')
                            print(name + ' does not appear in any decade.')
                    except:
                        print('Invalid output.')


                # Option 2
                elif choice == 2:
                    try:
                        name = input('Enter a name: ')
                        print(' ')

                        #Print all the rankings in one line
                        strng=''
                        for i in babyNames[name]:
                            strng=strng+ str(i) +' '
                        print (name +": "+ strng)

                        #Print all the rankings in separate lines
                        k=0
                        for i in range(1900, 2010, 10):
                            print(str(i) + ': ' + str(babyNames[name][k]))
                            k += 1
                    except:
                        print('Invalid input.')


                # Option 3
                elif choice == 3:
                    try:
                        decade = int(input('Enter decade:'))
                        dict = {}
                        dec = int(decade % 1900 / 10) #Convert decade to index

                        #Put all names with the rankings in that specific decade into a dictionary
                        for key in babyNames:
                            if babyNames[key][dec] != 0:
                                dict[key] = babyNames[key][dec]

                        #Sort the dictionary based on the values
                        sortedDict = sorted(dict.items(), key=lambda x: x[1])

                        #Print nicely
                        for i in range(len(sortedDict)):
                            print(sortedDict[i][0]+": "+str(sortedDict[i][1]))
                    except:
                        print("Invalid input.")


                # Option 4
                elif choice == 4:
                    #Create a dictionary that uses years as keys and names as values
                    years= {1900:[], 1910 : [],1920 : [],1930 : [],1940 : [],1950 : [],1960 : [],1970 : [],1980 : [],1990 : [],2000 : []}
                    for key in babyNames:
                        a = 0
                        for i in range(1900, 2010, 10):
                            if babyNames[key][a]!=0:
                                years[i].append(key)
                                a+=1


                    #Find the common names that appers in every values(lists). But in order to use the special function of set, convert the lists into sets
                    s=set(set(years[1900]))&set(years[1910])&set(years[1920])&set(years[1930])&set(years[1940])&set(years[1950])&set(years[1960])&set(years[1970])&set(years[1980])&set(years[1990])&set(years[2000])
                    sortedS=sorted(s)   #Sort the set

                    #Print nicely
                    print(str(len(sortedS))+' names appear in every decade. The names are: ')
                    for i in sortedS:
                        print(i)


                # Option 5
                elif choice == 5:
                    nameListMore=[]

                    #Find all the names and append them into a list
                    for key in babyNames:
                        if morePopular(babyNames[key]):
                            nameListMore.append(key)

                    #Count how many names
                    print(str(len(nameListMore))+' names are more popular in every decade')

                    #Print nicely
                    for i in nameListMore:
                        print(i)

                    #Replace all 1001s to 0s
                    backToOriginal(babyNames)


                # Option 6
                elif choice == 6:
                    nameListLess = []

                    # Find all the names and append them into a list
                    for key in babyNames:
                        if lessPopular(babyNames[key]):
                            nameListLess.append(key)

                    # Count how many names
                    print(str(len(nameListLess)) + ' names are less popular in every decade')
                    for i in nameListLess:
                        print(i)

                    # Replace all 1001s to 0s
                    backToOriginal(babyNames)

            else:
                break
        except:
            print('Invalid input.')
        finally:
            print(' ')


    print('Goodbye.') #Will printout Goodbye if the input is an int and is not within 1-6




main()
