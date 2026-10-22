import numpy as np
from scipy import stats

arr = np.array([4, 8, 15, 16, 23, 42])

print("mean: ",stats.tmean(arr))
print("median: ",np.median(arr))
print("variance: ",stats.tvar(arr,ddof=0))
print("standard deviation: ",np.std(arr))

