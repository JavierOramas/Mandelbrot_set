import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,10000)
y = np.linspace(-1,1,10000)

x_axis = []
y_axis = []

def mandel(c):

    z = 0
    for i in range(0,10):
        z = z**2 + c
    
    return z 

def mandel_set(x,y):
    for i in x:
        for z in y:
            a = complex(i+z*((-1)**(-1/2)))
            m = mandel(a)
            if abs(m) < 2:
                x_axis.append(i)
                y_axis.append(z)

if __name__ == '__main__':
    mandel_set(x,y)
    plt.scatter(x_axis, y_axis)
    plt.savefig('test.jpeg')
    plt.show()