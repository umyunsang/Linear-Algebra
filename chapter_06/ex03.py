import numpy as np


def tripleProduct(u, v, w):
    M = np.zeros((3, 3))
    M[0:] = u
    M[1:] = v
    M[2:] = w
    val = np.linalg.det(M)
    return val


A = np.array([1, 2, 3])
B = np.array([0, 5, 2])
C = np.array([2, 2, 4])
D = np.array([2, 4, 1])
u = B - A
v = C - A
w = D - A
val = tripleProduct(u, v, w)
print("부피 : ", np.absolute(val))
