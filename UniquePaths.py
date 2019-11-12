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

def count_paths(Start, End):
    # <Feel free to write helper functions if you need to>
    pass

def print_paths(Start, End): #BONUS QUESTION 15 points
    # <Feel free to write helper functions if you need to>
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
