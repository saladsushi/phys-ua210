#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt

## setting the given mean and standard deviation
mean = 0
sd = 3

## setting the x values
x = np.linspace(-10, 10, 1000, endpoint = True)

## setting the Gaussian. 2.507 is the approximate value for square root of 2π
y = 1/(sd*2.507)*np.exp(-0.5 *((x-mean)/sd)**2)

plt.plot(x,y)
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.title('Gaussian Distribution')

plt.savefig('gaussian.png')
plt.show()


# In[ ]:
