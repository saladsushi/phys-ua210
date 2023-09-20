from math import sqrt
import numpy as np
import timeit
import matplotlib.pyplot as plt


##Question 1
number = 121
print('Question 1: ', bin(number)[2:])






##Question 2
##for loop method
def forloop(L):
    M = 0.0
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if (i == j == k == 0): ##ignore the origin
                    continue

                a = 1.0/sqrt(i**2 + j**2 + k**2)

                if (i+j+k)%2 == 0: ## odd and even
                    a *= -1

                M += a
    return M
starttime1 = timeit.default_timer()
print('\nQuestion 2: ')
print('The Madelung constant for nacl is: ',forloop(150))
print('For loop method elapsed time in seconds: ',timeit.default_timer() - starttime1)

## array method
def arraymethod (L):
    i = np.arange(-L, L+1)[:, np.newaxis, np.newaxis]
    j = np.arange(-L, L+1)[:, np.newaxis]
    k = np.arange(-L, L+1)

    sum_of_squares = i**2 + j**2 + k**2

    ## avoid dividing by 0
    sum_of_squares[sum_of_squares == 0] = 1
    arr = np.sqrt(1.0 / sum_of_squares)

    ## make the origin 0 so that it does not have an effect on the sum
    arr[L,L,L] = 0

    ## odd and even
    plusminus = (i+j+k)%2
    arr[plusminus == 0] *= -1

    M = np.sum(arr)
    return M


starttime2 = timeit.default_timer()
print('\nThe Madelung constant for nacl is: ',arraymethod(150))

print('Array method elapsed time in seconds: ',timeit.default_timer() - starttime2)







##Question 3

print('\nQuestion 3 (plot is created): ')
N = 500 ## grid size
x_min, x_max = -2, 2
y_min, y_max = -2, 2
iter = 120  ## number of iterations

x_values = np.linspace(-2, 2, N)
y_values = np.linspace(-2, 2, N)
mandelbrot = np.zeros((N, N))

## Mandelbrot set
for i, x in enumerate(x_values):
    for j, y in enumerate(y_values):
        c = complex(x, y) ## complex values
        z = 0
        for k in range(iter):
            z = z**2 + c
            if abs(z) > 2: ## eliminate the unqualified values
                break
        mandelbrot[i, j] = k


plt.imshow(mandelbrot.T, extent=[x_min, x_max, y_min, y_max], cmap='hot') ## transpose the array
plt.title('Mandelbrot Set')
plt.xlabel('Re')
plt.ylabel('Im')
plt.savefig('Mandelbrot_Set.png')
plt.show()







##Question 4
##Part a
def solution_a (a, b, c):
    root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return root1, root2

print('\nQuestion 4 Part a:\nThe roots are: ', solution_a(0.001, 1000, 0.001))

##Part b
def solution_b (a, b, c):
    root1 = (2*c) / (-b + sqrt(b**2 - 4*a*c))
    root2 = (2*c) / (-b - sqrt(b**2 - 4*a*c))
    return root1, root2

print('\nPart b:\nThe roots are: ', solution_b(0.001, 1000, 0.001))

##Part c
##The error stems from discriminant term because when b is positive and much
##larger than a and c, the discriminant term will be very close to b. When we
##calculate -b+discriminant the two terms nearly cancel each other out due to
##the inaccuracy in float numbers in python. So we need to switch up the formulas
##in the fashion shown below.
def solution_c (a, b, c):

    if b >= 0:
        root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        root2 = (2*c) / (-b - sqrt(b**2 - 4*a*c))
    else:
        root1 = (2*c) / (-b + sqrt(b**2 - 4*a*c))
        root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    return root1, root2
print('\nPart c:\nThe roots are: ', solution_c(0.001, 1000, 0.001))
