import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# Part a
# Constants
M = 9.109e-31
L = 1e-8
N = 1000
a = L / N
h_bar = 1.05e-34
i_h_bar = 1j * h_bar   # i * h_bar

x0 = L / 2
sigma = 1e-10
k = 5e10

h = 1e-18
x = np.linspace(0, L, N)
psi_0 = np.exp(-((x - x0)**2) / (2 * sigma**2)) * np.exp(1j * k * x)

psi_0[0] = psi_0[-1] = 0

a1 = 1 + h * i_h_bar / (2 * M * a**2)
a2 = - h * i_h_bar / (4 * M * a**2)
b1 = 1 - h * i_h_bar / (2 * M * a**2)
b2 = h * i_h_bar / (4 * M * a**2)

diagonals_A = [a1 * np.ones(N), a2 * np.ones(N-1), a2 * np.ones(N-1)]
A = diags(diagonals_A, [0, -1, 1], format="csc")
diagonals_B = [b1 * np.ones(N), b2 * np.ones(N-1), b2 * np.ones(N-1)]
B = diags(diagonals_B, [0, -1, 1], format="csc")

v = B.dot(psi_0)

psi_t_h = spsolve(A, v)
psi_t_h[:5], psi_t_h.shape



# Part b
psi_t = psi_0.copy()

num_time_steps = 1000
t = 100

wavefunctions = [psi_t.real]

for step in range(1, num_time_steps + 1):
    psi_t = spsolve(A, B.dot(psi_t))
    if step % t == 0:
        wavefunctions.append(psi_t.real)

plt.figure(figsize=(14, 8))

for i, wf in enumerate(wavefunctions):
    plt.plot(x, wf, label=f'Step {i * t}')

plt.title('Real part of the wavefunction at different times')
plt.xlabel('Position (m)')
plt.ylabel('Real part of ψ')
plt.legend()
plt.grid(True)
plt.show()



# Part c
# the system is demonstrating how the probability distribution of a quantum
# particle evolves over time according to the principles of quantum mechanics.
