import numpy as np
from scipy import stats

height = np.array([150, 155, 160, 162, 165, 168, 170, 175, 178, 180])

weight = np.array([50, 52, 55, 58, 60, 62, 65, 70, 72, 75])

r,p_value = stats.pearsonr(height,weight)

print("correlation coefficient: ",r)
print("p_vlaue: ",p_value)


if p_value < 0.05:
    print("height and weight are significantly correlated")
else:
    print("there is no statistically significant correlation")