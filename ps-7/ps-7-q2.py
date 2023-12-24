import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('survey.csv')
data.head()

def log_funct(x, beta_0, beta_1):
    return 1.0 / (1.0 + np.exp(-(beta_0 + beta_1 * x)))

def neg_log(params, x, y):
    beta_0, beta_1 = params
    prob = log_funct(x, beta_0, beta_1)
    prob = np.clip(prob, 1e-10, 1 - 1e-10)
    log_prob = y * np.log(prob) + (1 - y) * np.log(1 - prob)
    return -np.sum(log_prob)

init = [0, 0]

ages = data['age'].values
recognized = data['recognized_it'].values

result = minimize(neg_log, init, args=(ages, recognized), method='BFGS')

beta_0_optimal, beta_1_optimal = result.x
beta_0_optimal, beta_1_optimal, result.fun


age_range = np.linspace(ages.min(), ages.max(), 1000)

prob = log_funct(age_range, beta_0_optimal, beta_1_optimal)
plt.scatter(data['age'], data['recognized_it'], alpha=0.5, label='Survey Data')
plt.plot(age_range, prob, color='red', label='Logistic Model')
plt.xlabel('Age')
plt.ylabel('Probability of Recognizing Phrase')
plt.title('Logistic Regression Model and Survey Data')
plt.legend()
plt.savefig('Logistic Regression Model and Survey Data')
plt.show()
