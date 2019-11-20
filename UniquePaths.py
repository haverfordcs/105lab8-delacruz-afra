# Find the number of unique possible paths from a given cell of a matrix to the end of the matrix
# For example, the number of possible paths from the cell 1 (coordinate (0,0)) to the cell 9 (coordinate (2,2))
# in the following maze is given as:
###################
# (1) # (2) # (3) #
###################
# (4) # (5) # (6) #
###################
# (7) # (8) # (9) #
###################
# The directions allowed to walk from a given cell are bottom, right, and diagonal (bottom-right),
# In the above case, the unique paths are 13, as given below:
# ['(1)->(2)->(5)->(8)->(9)', '(1)->(2)->(5)->(9)', '(1)->(2)->(5)->(6)->(9)', '(1)->(2)->(6)->(9)', '(1)->(2)->(3)->(6)->(9)', '(1)->(4)->(7)->(8)->(9)', 
# '(1)->(4)->(8)->(9)', '(1))->(4)->(5)->(8)->(9)', '(1)->(4)->(5)->(9)', '(1)->(4)->(5)->(6)->(9)', '(1)->(5)->(8)->(9)', '(1)->(5)->(9)', '(1)->(5)->(6)->(9)'] 
# not necessarily in order
##########################################################################
###### EARN BONUS of 15 points BY IMPLEMENTING print_paths(Start, End)####
##########################################################################

'''
Count and print path testing...

>>> import UniquePaths as UP
>>> UP.count_paths((0,0), (0,0)) == 1
True
>>> UP.count_paths((0,0), (1,1)) == 3
True
>>> UP.count_paths((0,0), (2,2)) == 13
True
>>> UP.count_paths((0,0), (3,3)) == 63
True
>>> UP.count_paths((1,0), (2,2)) == 5
True
>>> UP.count_paths((1,1), (2,2)) == 3
True
>>> sorted(UP.print_paths((0,0), (1,1)))
['(1)->(2)->(4)', '(1)->(3)->(4)', '(1)->(4)']
>>> sorted(UP.print_paths((0,0), (2,2)))
['(1)->(2)->(3)->(6)->(9)', '(1)->(2)->(5)->(6)->(9)', '(1)->(2)->(5)->(8)->(9)', '(1)->(2)->(5)->(9)', '(1)->(2)->(6)->(9)', '(1)->(4)->(5)->(6)->(9)', '(1)->(4)->(5)->(8)->(9)', '(1)->(4)->(5)->(9)', '(1)->(4)->(7)->(8)->(9)', '(1)->(4)->(8)->(9)', '(1)->(5)->(6)->(9)', '(1)->(5)->(8)->(9)', '(1)->(5)->(9)']
>>> sorted(UP.print_paths((0,0), (3,3)))
['(1)->(2)->(3)->(4)->(8)->(12)->(16)', '(1)->(2)->(3)->(7)->(11)->(12)->(16)', '(1)->(2)->(3)->(7)->(11)->(15)->(16)', '(1)->(2)->(3)->(7)->(11)->(16)', '(1)->(2)->(3)->(7)->(12)->(16)', '(1)->(2)->(3)->(7)->(8)->(12)->(16)', '(1)->(2)->(3)->(8)->(12)->(16)', '(1)->(2)->(6)->(10)->(11)->(12)->(16)', '(1)->(2)->(6)->(10)->(11)->(15)->(16)', '(1)->(2)->(6)->(10)->(11)->(16)', '(1)->(2)->(6)->(10)->(14)->(15)->(16)', '(1)->(2)->(6)->(10)->(15)->(16)', '(1)->(2)->(6)->(11)->(12)->(16)', '(1)->(2)->(6)->(11)->(15)->(16)', '(1)->(2)->(6)->(11)->(16)', '(1)->(2)->(6)->(7)->(11)->(12)->(16)', '(1)->(2)->(6)->(7)->(11)->(15)->(16)', '(1)->(2)->(6)->(7)->(11)->(16)', '(1)->(2)->(6)->(7)->(12)->(16)', '(1)->(2)->(6)->(7)->(8)->(12)->(16)', '(1)->(2)->(7)->(11)->(12)->(16)', '(1)->(2)->(7)->(11)->(15)->(16)', '(1)->(2)->(7)->(11)->(16)', '(1)->(2)->(7)->(12)->(16)', '(1)->(2)->(7)->(8)->(12)->(16)', '(1)->(5)->(10)->(11)->(12)->(16)', '(1)->(5)->(10)->(11)->(15)->(16)', '(1)->(5)->(10)->(11)->(16)', '(1)->(5)->(10)->(14)->(15)->(16)', '(1)->(5)->(10)->(15)->(16)', '(1)->(5)->(6)->(10)->(11)->(12)->(16)', '(1)->(5)->(6)->(10)->(11)->(15)->(16)', '(1)->(5)->(6)->(10)->(11)->(16)', '(1)->(5)->(6)->(10)->(14)->(15)->(16)', '(1)->(5)->(6)->(10)->(15)->(16)', '(1)->(5)->(6)->(11)->(12)->(16)', '(1)->(5)->(6)->(11)->(15)->(16)', '(1)->(5)->(6)->(11)->(16)', '(1)->(5)->(6)->(7)->(11)->(12)->(16)', '(1)->(5)->(6)->(7)->(11)->(15)->(16)', '(1)->(5)->(6)->(7)->(11)->(16)', '(1)->(5)->(6)->(7)->(12)->(16)', '(1)->(5)->(6)->(7)->(8)->(12)->(16)', '(1)->(5)->(9)->(10)->(11)->(12)->(16)', '(1)->(5)->(9)->(10)->(11)->(15)->(16)', '(1)->(5)->(9)->(10)->(11)->(16)', '(1)->(5)->(9)->(10)->(14)->(15)->(16)', '(1)->(5)->(9)->(10)->(15)->(16)', '(1)->(5)->(9)->(13)->(14)->(15)->(16)', '(1)->(5)->(9)->(14)->(15)->(16)', '(1)->(6)->(10)->(11)->(12)->(16)', '(1)->(6)->(10)->(11)->(15)->(16)', '(1)->(6)->(10)->(11)->(16)', '(1)->(6)->(10)->(14)->(15)->(16)', '(1)->(6)->(10)->(15)->(16)', '(1)->(6)->(11)->(12)->(16)', '(1)->(6)->(11)->(15)->(16)', '(1)->(6)->(11)->(16)', '(1)->(6)->(7)->(11)->(12)->(16)', '(1)->(6)->(7)->(11)->(15)->(16)', '(1)->(6)->(7)->(11)->(16)', '(1)->(6)->(7)->(12)->(16)', '(1)->(6)->(7)->(8)->(12)->(16)']
>>> sorted(UP.print_paths((2,1), (3,3)))
['(10)->(11)->(12)->(16)', '(10)->(11)->(15)->(16)', '(10)->(11)->(16)', '(10)->(14)->(15)->(16)', '(10)->(15)->(16)']

'''

def count_paths(Start, End):
   # <Feel free to write helper functions if you need to>
   if Start == End:  #base case
       return 1
   elif Start[0]<End[0] and Start[1]<End[1]:  #if Start is to the left of and above End
       return count_paths((Start[0]+1, Start[1]), End) + count_paths((Start[0], Start[1]+1), End) + count_paths((Start[0]+1, Start[1]+1), End)
   elif Start[0] == End[0]:  #if Start is in the same column as End
       return count_paths((Start[0], Start[1]+1), End)
   else:  #if Start is in the same row as End
       return count_paths((Start[0]+1, Start[1]), End)

   pass

def print_paths(Start, End): #BONUS QUESTION 15 points
   # <Feel free to write helper functions if you need to>
   def findpaths(Start, End):
       if Start == End:  #Base case
           return [str(Start)]
       elif Start[0] < End[0] and Start[1] < End[1]:   #if Start is to the left of and above End
           paths = findpaths((Start[0] + 1, Start[1]), End) + findpaths((Start[0], Start[1] + 1), End) + findpaths((Start[0] + 1, Start[1] + 1), End)
           output = []
           for path in paths:
               output.append(str(Start)+ "->" + path)
           return output
       elif Start[0] == End[0]:  #if Start is in the same column as End
           paths = findpaths((Start[0], Start[1] + 1), End)
           output = []
           for path in paths:
               output.append(str(Start)+ "->" + path)
           return output
       else:  #if Start is in the same row as End
           paths = findpaths((Start[0] + 1, Start[1]), End)
           output = []
           for path in paths:
               output.append(str(Start) + "->" + path)
           return output
   print(findpaths(Start, End))
   pass

if __name__ == "__main__":
    start = (0, 0)
    end = (2, 2)
    if count_paths(start, end) == 13:
        print('Passed for {} and {}'.format(start, end))
    else:
        print('Failed for {} and {}'.format(start, end))

    start = (1, 0)
    end = (2, 2)
    if count_paths(start, end) == 5:
        print('Passed for {} and {}'.format(start, end))
    else:
        print('Failed for {} and {}'.format(start, end))

    start = (1, 1)
    end = (2, 2)
    if count_paths(start, end) == 3:
        print('Passed for {} and {}'.format(start, end))
    else:
        print('Failed for {} and {}'.format(start, end))

    start = (0, 0)
    end = (3, 3)
    if count_paths(start, end) == 63:
        print('Passed for {} and {}'.format(start, end))
    else:
        print('Failed for {} and {}'.format(start, end))

