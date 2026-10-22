from scipy.optimize import root

def f(x):
    return x[0]**3 - 4*x - 9

result = root(f, x0=2)

print("root: ",result.x[0])