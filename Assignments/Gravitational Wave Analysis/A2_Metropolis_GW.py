import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def h(t, alpha, beta, gamma):
    return alpha*np.exp(t)*(1-np.tanh(2*(t-beta)))*np.sin(gamma*t)

# Extracting data
data_path = "Assignments/Gravitational Wave Analysis/gw_data.csv"
ht_data = pd.read_csv(data_path)

# I want to deal with np arrays
ts = np.array(ht_data["t"])
hs = np.array(ht_data["h"])

# 0 < a < 2, 1 < b < 10, 1 < c < 20
a = 1.0
step_a = 0.05

b = 5.5
step_b = 0.05

c = 10.5
step_c = 0.1

# Maximum |h| value of dataset
m = np.min(hs)
M = np.max(hs)
M = M if (abs(M)>abs(m)) else abs(m)

# Computing Y value for a particular (a,b,c)
def log_P(ts:np.ndarray, hs:np.ndarray, a, b, c):
    Y = np.sum((hs-h(ts, a, b, c))**2)/((0.2*M)**2)
    return (-1*Y)

# Metropolis Step
burn_in = 3000
N = 50000
pts = np.zeros((N,3))

for i in range(burn_in+N):
    new_a = np.random.normal(a,step_a)
    new_b = np.random.normal(b,step_b)
    new_c = np.random.normal(c,step_c)

    # Makes sure new values are within bounds
    if not (0<new_a<2) & (1<b<10) & (1<c<20): continue

    # Check probability at current (a,b,c) vs new (a,b,c)
    log_acc = log_P(ts, hs, new_a, new_b, new_c) - log_P(ts, hs, a, b, c)
    r = np.random.uniform(0,1)
    if np.log(r) < log_acc: # Issues encountered with exponential, so eliminated it entirely
        a = new_a
        b = new_b
        c = new_c
    if i >= burn_in: pts[i-burn_in] = np.array([a,b,c])

# Checking Values:
mean_a = np.mean(pts[:,0])
mean_b = np.mean(pts[:,1])
mean_c = np.mean(pts[:,2])

print(r"Mean Alpha:", mean_a)
print(r"Mean Beta: ", mean_b)
print(r"Mean Gamma:", mean_c)

# Plotting bins of Values of each parameter
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
ax[0].hist(pts[:, 0], bins=200, density=True)
ax[0].set_xlabel(r"$\alpha$")
ax[0].set_ylabel(r"$\propto$ Probability density")
ax[0].axvline(mean_a, color="red", linestyle="--", linewidth=1, label=f"Mean = {mean_a:.3f}")
ax[0].set_title(r"Metropolis on $\alpha$")
plt.legend()

ax[1].hist(pts[:, 1], bins=200, density=True)
ax[1].set_xlabel(r"$\beta$")
ax[1].set_ylabel(r"$\propto$ Probability density")
ax[1].axvline(mean_b, color="red", linestyle="--", linewidth=1, label=f"Mean = {mean_b:.3f}")
ax[1].set_title(r"Metropolis on $\beta$")
plt.legend()

ax[2].hist(pts[:, 2], bins=200, density=True)
ax[2].set_xlabel(r"$\gamma$")
ax[2].set_ylabel(r"$\propto$ Probability density")
ax[2].axvline(mean_c, color="red", linestyle="--", linewidth=1, label=f"Mean = {mean_c:.3f}")
ax[2].set_title(r"Metropolis on $\gamma$")
plt.legend()

plt.tight_layout()

# Plotting the final graph to verify
plt.figure(figsize=(12, 5))
plt.scatter(ts,hs,s=5,alpha=0.25,label="Data")
plt.plot(ts,h(ts, mean_a, mean_b, mean_c), linewidth=2,label="Predicted Function",color="orange")

plt.xlabel("$t$")
plt.ylabel("$h(t)$")
plt.title("Metropolis-Hastings Fit")
plt.legend()
plt.grid(alpha=0.2)

plt.show()