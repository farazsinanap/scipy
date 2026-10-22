from scipy.optimize import minimize

def f(x):
    return x[0]**2 + 5*x[0] + 6

result = minimize(f, x0=[0])
print("value of x: ",result.x[0])
print("minimum value: ",result.fun)