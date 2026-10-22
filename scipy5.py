from scipy import stats

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 40, 50, 55, 65, 70]

result = stats.linregress(hours,marks)

print("slope: ",result.slope)
print("intercept: ",result.intercept)
print("correltation coefficient: ",result.rvalue)
print("p_vlaue: ",result.pvalue)
print("linear equation: y =", result.slope, " x +", result.intercept) 