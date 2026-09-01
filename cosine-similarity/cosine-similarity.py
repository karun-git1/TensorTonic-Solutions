import numpy as np
import math
def cosine_similarity(a,b):
    dot=0
    n_a=0
    n_b=0
    for i in range(len(a)):
        dot+=a[i]*b[i]
        n_a+=a[i]*a[i]
        n_b+=b[i]*b[i]
    n_a=math.sqrt(n_a)
    n_b=math.sqrt(n_b)
    if n_a==0 or n_b==0:
        return 0.0
    
    return float(dot/(n_a*n_b))