# Defining main function
import numpy as np

def f(x):
    return np.sin(x)


def main():
    eps = 1e-14
    x0 = 2
    x1 = 4
    while np.abs(f(x1))>eps:
        temp=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = temp
        print(f"x = {x1}")

    print()
    print(f"root: x= {x1}, f(x1) = {f(x1)}")

  
  
if __name__=="__main__":
    main()
