from scipy.stats import binom

n = 20
p = 0.05
x = 3

probability = binom.pmf(x,n,p)


print("probability: ",probability)
print("percentage: ",probability * 100,"%")