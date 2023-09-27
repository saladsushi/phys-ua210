import numpy as np
import matplotlib.pyplot as plt
def explicit_matrix_mult(N):
    count = 0
    ##create A and B arrays
    A = np.ones([N,N], float)
    B = np.ones([N,N], float)
    B *= 2
    ##generate array C
    C = np.zeros([N,N], float)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,k]*B[k,j]
                ##count the number of operations
                count+=1
    return count, C

def dot_method (N):
    A = np.ones([N,N], float)
    B = np.ones([N,N], float)
    B *= 2
    ##generate array C
    C = np.dot(A, B)
    return C

x = np.zeros(5)
y = np.zeros(5)
x1 = explicit_matrix_mult(30)
print(x1[1])
print(dot_method(30))
x[0] = 30
y[0] = x1[0]

x2 = explicit_matrix_mult(60)
dot_method(60)
print(x2[1])
print(dot_method(60))
x[1] = 60
y[1] = x2[0]

x3 = explicit_matrix_mult(90)
dot_method(90)
print(x3[1])
print(dot_method(90))
x[2] = 90
y[2] = x3[0]

x4 = explicit_matrix_mult(120)
dot_method(120)
print(x4[1])
print(dot_method(120))
x[3] = 120
y[3] = x4[0]

x5 = explicit_matrix_mult(150)
dot_method(150)
print(x5[1])
print(dot_method(150))
x[4] = 150
y[4] = x5[0]
print(x,'\n', y)


plt.scatter(x,y)
plt.plot(x, y)
plt.xlabel('Size of the Matrix')
plt.ylabel('Number of Operations')
plt.title('Relationship Between Size and Operations')

plt.savefig('matrix.png')
plt.show()
