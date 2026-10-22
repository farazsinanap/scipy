import numpy as np
from scipy.interpolate import interp1d

time = np.array([1, 2, 3, 4, 5])
temperature = np.array([20, 25, np.nan, 35, 40])

valid = ~np.isnan(temperature)
f = interp1d(time[valid], temperature[valid])

temperature[np.isnan(temperature)] = f(time[np.isnan(temperature)])
print("temperature: ",temperature)