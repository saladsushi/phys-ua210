import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

tau_Bi213 = 46 * 60
tau_Tl209 = 2.2 * 60
tau_Pb209 = 3.3 * 60

n_Bi213 = 10000
n_Tl209 = n_Pb209 = n_Bi209 = 0

# Time step and total time
dt = 1
total_time = 20000

# Lists to store atom counts over time
Bi213_count, Tl209_count, Pb209_count, Bi209_count = [], [], [], []

# Main loop
for t in range(0, total_time, dt):
    # Part A
    decayed_Pb209 = np.sum(np.random.rand(n_Pb209) < (1 - 2**(-dt/tau_Pb209)))
    n_Pb209 -= decayed_Pb209
    n_Bi209 += decayed_Pb209

    # Part B
    decayed_Tl209 = np.sum(np.random.rand(n_Tl209) < (1 - 2**(-dt/tau_Tl209)))
    n_Tl209 -= decayed_Tl209
    n_Pb209 += decayed_Tl209

    # Part C
    decayed_Bi213 = np.sum(np.random.rand(n_Bi213) < (1 - 2**(-dt/tau_Bi213)))
    n_Bi213 -= decayed_Bi213
    decayed_to_Tl209 = np.sum(np.random.rand(decayed_Bi213) < 0.0209)
    n_Tl209 += decayed_to_Tl209
    n_Pb209 += (decayed_Bi213 - decayed_to_Tl209)

    Bi213_count.append(n_Bi213)
    Tl209_count.append(n_Tl209)
    Pb209_count.append(n_Pb209)
    Bi209_count.append(n_Bi209)

# Plot results
plt.plot(Bi213_count, label='Bi213')
plt.plot(Tl209_count, label='Tl209')
plt.plot(Pb209_count, label='Pb209')
plt.plot(Bi209_count, label='Bi209')
plt.xlabel('Time (s)')
plt.ylabel('Number of Atoms')
plt.title('Decay of Bi213 Atoms')
plt.savefig('Bi213 Decay')
plt.legend()
plt.show()
