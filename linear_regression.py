import numpy as np
import matplotlib.pyplot as plt


def estimated_coef(X,Y):
    mean_x =0
    mean_y =0
    for i in range(len(X)):
        mean_x += X[i]
        mean_y += Y[i]
    mean_x = mean_x / len(X)
    mean_y = mean_y / len(Y)
    a1 = 0
    a2 = 0
    for i in range(len(X)):
        a1 += X[i]*Y[i] - mean_x*mean_y
        a2 += X[i]*X[i] - mean_x*mean_x
    a = a1 / a2
    b = mean_y -a*mean_x
    return (a,b)

def plot_regression_line(X, Y, b):  
    plt.scatter(X, Y, color = "m", 
               marker = "o", s = 30) 
    regress = b[0] + b[1]*X 
    plt.plot(X, regress, color = "g")  
    plt.xlabel('x') 
    plt.ylabel('y')  
    plt.show() 
  

def main():  
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
    b = estimated_coef(x, y) 
    plot_regression_line(x, y, b) 
  
if __name__ == "__main__": 
    main() 
