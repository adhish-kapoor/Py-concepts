import numpy
a=list(map(float,input().split())) #input array
print(numpy.floor(a))               #prints floor value of all elements of a
print(numpy.ceil(a))                  #prints ceil value of all elements of a
print(numpy.rint(a))                    #rint(a) rounds to the nearest integer of all elements of a

#shape and reshape tool
import numpy
a=list(map(int,input().split()))  # 1 2 3 4 5 6 7 8 9
a1=numpy.array(a)
a1.shape=(3,3)                    # 3 rows 3 columns
print(a1)   #[[1 2 3]
            # [4 5 6]
            # [7 8 9]]



