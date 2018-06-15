#set() is an unordered collection of distinct elements 

print(set([1,2,2,1,3,8,7,5,9])) 
                               # output is {1, 2, 3, 5, 7, 8, 9}
print(set("ADHISH"))
                               # output is {'I', 'S', 'H', 'A', 'D'}
                               
#len() is a function that gives length of a string

print(len("ADHISH"))           #output 6
print(len(set("ADHISH")))      #output 5

#itertools.groupby() function
#groupby() generates a break or new group every time the value of the key function changes 
#(which is why it is usually necessary to have sorted the data using the same key function).

import itertools as it
print(' '.join(('({}, {})'.format(len(list(g)), x) for x,g in it.groupby(input())))) # input 1222311 #output (1, 1) (3, 2) (1, 3) (2, 1)
