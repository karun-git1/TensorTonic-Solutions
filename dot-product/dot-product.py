import numpy as np

def dot_product(x, y):
    result=0
    for i in range (len(x)):
        result+=x[i]*y[i]
    return float(result)