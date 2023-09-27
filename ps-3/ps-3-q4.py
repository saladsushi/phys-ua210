import numpy as np
import matplotlib.pyplot as plt


tau = 3.053 * 60  # half-life
num_atoms = 1000

uniform_random_numbers = np.random.uniform(0, 1, num_atoms)

# Apply the inverse of the CDF to transform the uniform random numbers
# The inverse CDF is derived from the CDF of the given distribution
decay_times = -tau * np.log2(1 - uniform_random_numbers)

# Sort decay times in ascending order
sorted_decay_times = np.sort(decay_times)

# Create an array representing the number of atoms that have not decayed
not_decayed_atoms = np.arange(num_atoms, 0, -1)

# Plot the number of atoms that have not decayed as a function of time
plt.plot(sorted_decay_times, not_decayed_atoms)
plt.xlabel('Time (s)')
plt.ylabel('Number of Atoms Not Decayed')
plt.title('Number of 208Tl Atoms Not Decayed Over Time')
plt.savefig('Atoms not decayed')
plt.show()
