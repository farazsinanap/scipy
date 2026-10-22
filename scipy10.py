from scipy.optimize import approx_fprime

def f(x):
    return x**3 + 2*x**2 + 5

x = 2
derivative = approx_fprime([x], lambda a: f(a[0]), 1e-6)


print("derivative at x =",x, ":",derivative[0])