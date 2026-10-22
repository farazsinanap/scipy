from scipy.integrate import quad

def f(x):
    return x**2 + 2*x + 1

result , error = quad(f,0,5)
print("integral: ",result)
print("error",error)