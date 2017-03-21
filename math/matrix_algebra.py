### Part 1 ###

import numpy as pd

A = np.matrix('1,2,3;2,7,4')
B = np.matrix('1,-1; 0,1')
C = np.matrix('5,-1; 9,1; 6,0')
D = np.matrix('3,-2,-1; 1,2,3')
u = np.array([6, 2, -3, 5])
v = np.array([3,5,-1,4])
w = np.matrix('1,8,0,5')

variable_list = [A, B, C, D, u, w]

for num, name in enumerate(variable_list, start=1):
    print("Question 1.{}: {}".format(num, name.shape))

### Part 2 ###
alpha = 6
print("Question 2.1: ", u+v)
print("Question 2.2: ", u-v)
print("Question 2.3: ", alpha*u)
print("Question 2.4: ", np.dot(u,v))
print("Question 2.5: ", np.linalg.norm(u))

### Part 3 ###
print("Question 3.1: ", "Not Defined")
print("Question 3.2: ", A - np.transpose(C))
print("Question 3.3: ", np.transpose(C) + 3*D)
print("Question 3.4: ", B*A)
print("Question 3.5: ", "Not Defined")

### OPTIONAL ###
print("Question 3.6", "Not Defined")
print("Question 3.7", C*B)
print("Question 3.8", np.linalg.matrix_power(B, 4))
print("Question 3.9", A * np.transpose(A))
print("Question 3.10",D * np.transpose(D))