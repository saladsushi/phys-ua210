from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# Part a
# Constants
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

def lorenz_system(t, Y):
    x, y, z = Y
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

Y0 = [0.0, 1.0, 0.0]
t_span = [0.0, 50.0]

solution = solve_ivp(lorenz_system, t_span, Y0, t_eval=np.linspace(t_span[0], t_span[1], 10000))

plt.figure(figsize=(12, 6))
plt.plot(solution.t, solution.y[1], label='y(t)')
plt.title('Lorenz System')
plt.xlabel('Time')
plt.ylabel('y')
plt.legend()
plt.show()

# Part b
plt.figure(figsize=(12, 6))
plt.plot(solution.y[0], solution.y[2], label='Lorenz Attractor')
plt.title('Lorenz Attractor')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.show()
