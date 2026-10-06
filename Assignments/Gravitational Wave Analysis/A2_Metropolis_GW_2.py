import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# true values ~ (1.4, 4, 10) probably, from least squares
# aryan's values ~ (0.05, 3.8, 10)
def h(t, alpha, beta, gamma):
    return alpha*np.exp(t)*(1-np.tanh(2*(t-beta)))*np.sin(gamma*t)

# Extracting data
data_path = "Assignments/Gravitational Wave Analysis/gw_data.csv"
ht_data = pd.read_csv(data_path)

# I want to deal with np arrays
ts = np.array(ht_data["t"])
hs = np.array(ht_data["h"])

a = 2
b = 3.5
c = 10 # fixed
true_h = h(ts, a, b, c)
aryan_h = h(ts, 0.05, 3.8, 10.0)

plt.scatter(ts, hs, label="Data", color="blue")
plt.plot(ts, true_h, label=f"Estimate ({a},{b},{c})", color="orange")
plt.plot(ts, aryan_h, label="Aryan's", color="red")
plt.xlabel("Time")
plt.legend()
plt.show()