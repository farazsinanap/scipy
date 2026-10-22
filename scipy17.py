import numpy as np
from scipy import stats

data = np.random.normal(loc=50,scale=10,size=30)

mean = np.mean(data)
se = stats.sem(data)


ci = stats.t.interval(0.95,df=len(data)-1,loc=mean,scale=se)

print("sample mean: ",mean)
print("95 % confidence interval: ",ci)