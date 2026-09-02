import numpy as np

def matrix_transpose(A):
    r=len(A)
    c=len(A[0])
    result=[]
    for j in range(c):
        row=[]
        for i in range(r):
            row.append(A[i][j])
        result.append(row)
    return np.array(result)
        
   