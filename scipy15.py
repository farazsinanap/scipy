from scipy.stats import poisson

average = 6
orders = 4

probability = poisson.pmf(orders,average)
print("probability: ",probability)
print("percentage: ",probability * 100,"%")