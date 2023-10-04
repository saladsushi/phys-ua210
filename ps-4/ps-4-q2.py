import numpy as np
import matplotlib.pyplot as plt

def integrand(x, a):
    return 1/np.sqrt(a**4 - x**4)

#/ !!This is a slice of code from University of Michigan, because the 'gaussxw' module
# from the textbook isn't available

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = np.linspace(3,4*N-1,N)/(4*N+2)
    x = np.cos(np.pi*a+1/(8*N*N*np.tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = np.ones(N,float)
        p1 = np.copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w


def gaussian_quadrature(a):
    N = 20
    #Weights and points for the Gaussian Quadrature for the interval [-1, 1]
    x, w = gaussxw(N)

    #Rescale the points and weights for the interval [0, a]
    x_rescaled = 0.5 * (a - 0) * x + 0.5 * (a + 0)
    w_rescaled = w * 0.5 * (a - 0)

    integral_value = np.dot(w_rescaled, integrand(x_rescaled, a))

    return np.sqrt(8) * integral_value

#starting from 0.01 to avoid division by zero
amplitudes = np.linspace(0.01, 2, 400)
periods = [gaussian_quadrature(a) for a in amplitudes]

plt.plot(amplitudes, periods)
plt.xlabel('Amplitude (a)')
plt.ylabel('Period (T)')
plt.title('Period vs. Amplitude for V(x) = x^4')
plt.savefig('Period vs. Amplitude.png')
plt.show()
