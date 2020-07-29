  
import numpy as np
import matplotlib.pyplot as plt
vec1 = np.array([-1., 4., -9.])
mat1 = np.array([[1., 3., 5.], [7., -9., 2.], [4., 6., 8.]])
vec2 = (np.pi/4) * vec1
vec2 = np.cos(vec2)
vec3 = vec1 + 2*vec2
vec4 = mat1*vec3
print("multiplication of mat1 and vec 3 is:", vec4)
#6
mat1 = mat1.transpose()
print("mat1 transpose is:" ,mat1)
#7
determinant = np.linalg.det(mat1)
print("determinant of mat1 is:", determinant)
#8

trace = np.trace(mat1)
print("trace of mat1 is", trace)
#9
smallestvec1 = np.min(vec1)
print("minimum value of vec1 is ", smallestvec1)
#10
j= np.where(vec1 == smallestvec1)
print("j is:", j)
#11
smallestmat1 = np.min(mat1)
print("minimum mat 1 ", smallestmat1)
#12
A= np.array([[17, 24, 1, 8, 15],
             [23, 5, 7, 14, 16],
             [4, 6, 13, 20, 22],
             [10, 12, 19, 21, 3],
             [11, 18, 25, 2, 9]])
colsum = np.sum(A,axis= -1)
rowsum = np.sum(A,axis= -2)
colmax = np.max(colsum)
colmin = np.min(colsum)
rowmax=  np.max(rowsum)
rowmin=  np.min(rowsum)
ghotrasl = np.sum(np.diag(A))
ghotrfaree= np.sum(np.diag(np.fliplr(A)))
if colmax ==rowmax and rowmax ==ghotrasl and ghotrasl == ghotrfaree :
   print("A IS MAGIC")
#13
M = np.random.rand(10,10)
print("M random is:", M)

#14
MUL = M[:5, :5]
MUR = M[:5,5:10]
MLL = M[5:10, :5]
MLR = M[5:10, 5:10]
print("MUL", MUL)
print("MUR", MUR)
print("MLL", MLL)
print("MLR", MLR)
