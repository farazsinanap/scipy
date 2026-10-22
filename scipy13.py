from scipy.stats import norm

mean = 50
std_dev = 10
x = 60 

probability = norm.cdf(x, loc=mean, scale=std_dev)



print("probablility: ",probability)
print("percentage: ",probability * 100,"%")