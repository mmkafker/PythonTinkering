####################################################################################################################
# We implement simulated annealing to find the minimum of a polynomial function in one or several variables.
# An initial position is chosen arbitrarily. It is randomly moved, and accepted unquestioningly if it decreases the
# function value. If it increases, it can be still be accepted, but the probability depends on the temperature, which
# is decreased as a function of iteration.
#####################################################################################################################



import numpy as np

# Single variate function
# def f(x):
#     return 3*x**2+2*x+1

# Multivariate function
def f(x,y,z):
    return 5*(x-3)**2 -2*x*y+3*x*z+y**2+4*z**2

def main():
    x = 0; y = 0; z = 0;
    alpha = 0.01
    T = 100
    Tmin = 1e-5
    #delta = 1e15
    while T>Tmin:
        xnew = x + alpha*(2*np.random.rand()-1) 
        ynew = y + alpha*(2*np.random.rand()-1)
        znew = z + alpha*(2*np.random.rand()-1)
        delta = f(x,y,z)-f(xnew,ynew,znew)
        if delta > 0:
            x = xnew
            y = ynew
            z = znew
        else:
            exponent = delta/T
            if np.abs(exponent) > 100:
                p = 0
            else:
                p = np.exp(exponent)
            if np.random.rand()<p:
                x = xnew
        T*=0.999
        print(f"(x,y,z) = ({x},{y},{z}), f(x,y,z) = {f(x,y,z)}, T = {T}")

    print(f"\nFinal Result: (x,y,z) = ({x},{y},{z}), f(x,y,z) = {f(x,y,z)}, T = {T}")
    #print(f"\nFinal Result: x = {x}, f(x) = {f(x)}")    
    

if __name__ == "__main__":
    main() 
