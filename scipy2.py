import numpy as np
from scipy.stats import norm

data = norm.rvs(size=1000)

mean = np.mean(data)
std_dev = np.std(data)

print("mean: ",mean)
print("standard deviation: ",std_dev)