#set() is an unordered collection of distinct elements 

print(set([1,2,2,1,3,8,7,5,9])) 
                               # output is {1, 2, 3, 5, 7, 8, 9}
print(set("ADHISH"))
                               # output is {'I', 'S', 'H', 'A', 'D'}
                               
#len() is a function that gives length of a string

print(len("ADHISH"))           #output 6
print(len(set("ADHISH")))      #output 5

#itertools.groupby()
#groupby() generates a break or new group every time the value of the key function changes 
#(which is why it is usually necessary to have sorted the data using the same key function).

import itertools as it
print(' '.join(('({}, {})'.format(len(list(g)), x) for x,g in it.groupby(input())))) # input 1222311 #output (1, 1) (3, 2) (1, 3) (2, 1)

#itertools.combinations()
#A = [1,1,3,3,3]
#print list(combinations(A,4))
#[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
from itertools import combinations
a=input()
s=a.split(' ')
s[0]=sorted(s[0])
b=[]
for i in range(1,int(s[1])+1,1):
    b.append(list(combinations(s[0],i)))

for i in range(0,len(b),1):
    for j in range(0,len(b[i]),1):
        print(*b[i][j],sep="")
#We can use the type() function to know which class a variable or a value belongs to and
#isinstance() function to check if it belongs to a particular class.
a = 5
# Output: <class 'int'>
print(type(a))

# Output: <class 'float'>
print(type(5.0))

# Output: (8+3j)
c = 5 + 3j
print(c + 3)

# Output: True
print(isinstance(c, complex))

#zfill() method returns a copy of the string with '0' chars padded to the left
# Takes a single parameter which is the length of the returned string
a="adhish kapoor"
print(a.zfill(15))            # output 00adhish kapoor

#find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
#The find() method takes maximum of three parameters:
#sub - It's the substring to be searched in the str string.
#start and end (optional) - substring is searched within str[start:end]
quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result) # output Substring 'let it': 11

#center() returns a string which is padded with the specified character.
#The center() method takes two arguments:
#width - length of the string with padded characters
#fillchar (optional) - padding character
string = "Python is awesome"
new_string = string.center(24, '*')    # '*' is fillchar
print("Centered String: ", new_string) # output Centered String:  ***Python is awesome****
