import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import hermite, roots_hermite, factorial
from scipy.integrate import quadrature

#/ !!This is originally a slice of code from University of Michigan, because the 'gaussxw' module
# from the textbook isn't available. I modified the code to aviod the type error.
def gaussxw(N):
    a = np.linspace(3, 4*N-1, N) / (4*N + 2)
    x = np.cos(np.pi * a + 1 / (8 * N * N * np.tan(a)))

    epsilon = 1e-15
    delta = 1.0
    while delta > epsilon:
        p0 = np.ones(N, float)
        p1 = np.copy(x)
        for k in range(1, N):
            p0, p1 = p1, ((2*k + 1) * x * p1 - k * p0) / (k + 1)
        dp = (N + 1) * (p0 - x * p1) / (1 - x * x)
        dx = p1 / dp
        x -= dx
        delta = max(abs(dx))
    w = 2 / ((1 - x**2) * dp**2)
    return x, w

# (a)
# Recursive Hermite polynomial
def H(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    else:
        return 2*x*H(n-1, x) - 2*(n-1)*H(n-2, x)

# Wave function phi
def phi(n, x):
    return (1/math.sqrt(2**n * math.factorial(n) * math.sqrt(np.pi))) * np.exp(-x**2/2) * H(n, x)

x = np.linspace(-4, 4, 400)
for n in range(4):
    plt.plot(x, phi(n, x), label=f'n={n}')

plt.legend()
plt.title("Harmonic Oscillator Wave Functions")
plt.xlabel("x")
plt.ylabel("phi_n(x)")
plt.savefig('Harmonic Oscillator Wave Functions.png')
plt.show()

#(b)
x = np.linspace(-10, 10, 1000)
plt.plot(x, phi(30, x))
plt.title("Harmonic Oscillator Wave Function for n=30")
plt.xlabel("x")
plt.ylabel("phi_30(x)")
plt.savefig('HOWF For n=30.png')
plt.show()

#(c)
def integrand(x, n):
    return x**2 * abs(phi(n, x))**2

N = 100
x, w = gaussxw(N)
a, b = -10, 10  # limits of integration
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

s = sum(wp * integrand(xp, 5))

print("Quantum uncertainty for n=5:", math.sqrt(s))

#(d)
def psi(n, x):
    normalization = 1 / np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))
    herm_poly = hermite(n)
    return normalization * np.exp(-x**2 / 2) * herm_poly(x)

def integrand_gh(x, n):
    return x**2 * abs(psi(n, x))**2 * np.exp(x**2)

def quantum_uncertainty(n):
    x, w = roots_hermite(100)
    integral = np.dot(integrand_gh(x, n), w)
    return np.sqrt(integral)

n = 5
print("Quantum uncertainty for n=5:", quantum_uncertainty(n))
