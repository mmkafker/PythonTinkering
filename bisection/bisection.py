import numpy as np

#def f(x):
#    return 1-x**2

def f(x):
    return np.sin(x)

def main():

    # Compute pi numerically by finding the root of sin(x)
    xl = 0.1
    xr = 4
    eps = 1e-15
    while np.abs(xr-xl)>eps:
        print(f"bound = {np.abs(xr-xl)}")
        x0 = (xl+xr)/2
        if f(x0) * f(xl) > 0:
            xl = x0
        else:
            xr = x0
    print()
    print(f"root = {(xr+xl)/2}")
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
