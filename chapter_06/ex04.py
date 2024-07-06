import numpy as np


def distPt2Pl(A, W, P):  # 거리 계산
    num = np.dot((P - A).T, W)
    deno = np.linalg.norm(W)
    val = np.absolute(num) / deno
    return val


A = np.array([2, 3, 4])
W = np.array([1, 2, 3])
P = np.array([0, 1, 2])
print("거리 : ", distPt2Pl(A, W, P))
