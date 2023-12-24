import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Part a
def integrand(x, a):
    return x**(a - 1) * np.exp(-x)

x = np.linspace(0, 5, 400)
a_val = [2, 3, 4]
integrand_values = {a: integrand(x, a) for a in a_val}

plt.figure(figsize=(10, 6))

for a in a_val:
    plt.plot(x, integrand_values[a], label=f'a = {a}')

plt.xlabel('x')
plt.ylabel('Integrand Value')
plt.title('Integrand of the Gamma Function for Various a')
plt.legend()
plt.grid(True)
plt.savefig('Integrand of the Gamma Function for Various a')
plt.show()

# Part b
# set the derivative of the integrand to 0:
# x^(a-2)(a-x-1)e^(-x) = 0
# only (a-x-1) can be 0, so x = a-1 is a critical point where the max. falls

# Part e
def gamma(a):
    c = 2 * (a - 1)
    def integrand(z):
        x = c * z / (1 - z)
        return (c * (x**(a - 1) * np.exp(-x))) / ((1 - z)**2)
    integral, _ = quad(integrand, 0, 1)
    return integral

print("The calculated value of Γ(1.5) is approximately: ", gamma(1.5))

# Part f
print("The calculated value of Γ(3) is approximately: ", gamma(3))
print("The calculated value of Γ(6) is approximately: ", gamma(6))
print("The calculated value of Γ(10) is approximately: ", gamma(10))
