import numpy as np


def angle2vectors(v, w):  # 두 벡터의 사잇각 계산
    vnorm = np.linalg.norm(v)
    wnorm = np.linalg.norm(w)
    vwdot = np.dot(v.T, w)
    angle = np.arctan(vwdot / (vnorm * wnorm)) * 360 / np.pi
    return angle


def orthProj(u, x):  # 정사영 계산
    xu_dot = np.dot(x.T, u)
    uu_dot = np.dot(u.T, u)
    projux = (xu_dot / uu_dot) * u
    return projux


A = np.array([[2], [4], [1]])
B = np.array([[1], [-1], [3]])
angle = angle2vectors(A, B)
projAB = orthProj(B, A)
print("A와 B의 사잇각 : ", angle)
print("A의 B 위로의 정사영 : \n", projAB)
