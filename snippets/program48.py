import numpy
a=numpy.matrix([[1,2,3,4],[5,6,7,8]])
print("withoutreshaping ->")
print(a)

b=numpy.reshape(a,-1)
print("HERE We don't know about what number we should give to row/col")
print("Reshaping as (a,-1)")
print(b)
