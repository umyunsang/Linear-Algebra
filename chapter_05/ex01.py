import numpy as np


def getMinorMatrix(A, i, j):  # 행렬 A의 i행과 j열을 제거하고 만든 행렬 생성
    n = len(A)
    M = np.zeros((n - 1, n - 1))
    for a in range(0, n - 1):
        k = a if (a < i) else a + 1
        for b in range(0, n - 1):
            l = b if (b < j) else b + 1
            M[a, b] = A[k, l]
    return M


def determinant(M):  # 행렬식 계산
    if len(M) == 2:  # 2x2 행렬의 행렬식 계산
        return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]

    detVal = 0
    for c in range(len(M)):
        detVal += ((-1) ** c) * M[0, c] * determinant(getMinorMatrix(M, 0, c))
    return detVal


A = np.array([[-4, 0, 2, -1, 0], [1, 3, -3, -1, 4], [2, 0, 1, 3, 0], [-2, 1, -3, -1, 5], [1, -5, 1, 0, 5]])
print("A =", A)
print("det(A) =", determinant(A))
