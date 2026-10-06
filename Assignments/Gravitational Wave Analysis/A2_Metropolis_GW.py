import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def h(t, alpha, beta, gamma):
    return alpha*np.exp(t)*(1-np.tanh(2*(t-beta)))*np.sin(gamma*t)

# Midpoint of ranges
# 0 < alpha < 2
a = 1.4
# 1 < beta < 10
b = 3.5
# 1 < gamma < 20
g = 10.5

# Extracting data
data_path = "Assignments/Gravitational Wave Analysis/gw_data.csv"
ht_data = pd.read_csv(data_path)

# I want to deal with np arrays
ts = np.array(ht_data["t"])
hs = np.array(ht_data["h"])

# Non-normalised Probability Computation
def log_prob_abg(t_arr:np.ndarray, h_arr:np.ndarray, a, b, g):
    Y = 0
    l = len(t_arr)
    for i in range(l):
        # Log-likelihood estimator
        Y -= (h_arr[i]-h(t_arr[i], a, b, g))**2/(0.04*h_arr[i]**2)
    return Y # probability is proportional to exp(Y), proportionality constant doesn't matter to metropolis

# Metropolis Step:
burn_in = 200
N = 10000
theta_cur = np.array([a,b,g]) # present theta value
thetas = np.zeros((N,3)) # All Sample Points

for i in range(burn_in+N): # Just update theta_cur until i >= burn_in
    new_a = np.random.normal(theta_cur[0], 0.01) # sufficiently small step
    new_b = np.random.normal(theta_cur[1], 0.08)
    new_g = np.random.normal(theta_cur[2], 0.1)
    if not ((0 < new_a < 2) & (1 < new_b < 10) & (1 < new_g < 20)):
        i -= 1
        continue

    a = 1.0 # Initialised to 1
    log_a = min(0,log_prob_abg(ts,hs,new_a,new_b,new_g)-log_prob_abg(ts,hs,theta_cur[0], theta_cur[1], theta_cur[2]))
    a = np.exp(log_a)
    r = np.random.uniform(0,1)
    if r < a:
        theta_cur[0] = new_a
        theta_cur[1] = new_b
        theta_cur[2] = new_g
    if i>=burn_in: thetas[i-burn_in] = theta_cur

# Plotting thetas:
plt.hist(thetas[:,0], bins=20) # alphas
plt.show()
plt.hist(thetas[:,1], bins=100) # betas
plt.show()
plt.hist(thetas[:,2], bins=100) # gammas
plt.show()