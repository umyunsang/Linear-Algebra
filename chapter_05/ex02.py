import numpy as np


def cofactor(A, i, j):  # 여인수 계산
    (n, m) = A.shape
    M = np.zeros((n - 1, m - 1))  # A[i, j]를 제외한 소행렬 M을 생성하기 위해 (n-1) x (m-1) 크기의 영행렬 생성
    for a in range(0, n - 1):
        k = a if (a < i) else a + 1  # A의 i행을 제외하여 소행렬의 행 인덱스 k 설정
        for b in range(0, m - 1):
            l = b if (b < j) else b + 1  # A의 j열을 제외하여 소행렬의 열 인덱스 l 설정
            M[a, b] = A[k, l]  # A의 i행과 j열을 제외한 부분 행렬이 소행렬 M에 저장

    return (-1) ** (i + j) * np.linalg.det(M)  # 여인수 = (-1)^(i+j) * M의 행렬식


def inverseByAdjointMatrix(A):  # 수반행렬을 이용한 A의 역행렬 계산
    detA = np.linalg.det(A)  # A의 행렬식 계산
    (n, m) = A.shape
    adjA = np.zeros((n, m))  # (n x m) 크기의 수반행렬 adjA를 초기화

    for i in range(0, n):  # 수반행렬 생성
        for j in range(0, m):
            adjA[j, i] = cofactor(A, i, j)  # adjA의 (j, i) 위치에 A의 (i, j) 원소에 대한 여인수(cofactor)를 할당

    if detA != 0.0:  # A의 행렬식이 0이 아닌 경우
        # 수반행렬 adjA를 이용한 역행렬 계산
        return (1. / detA) * adjA  # A의 역행렬 = (1/detA) * adjA
    else:
        return 0  # A의 행렬식이 0인 경우, 역행렬이 존재하지 않음


# 예시 행렬 A
A = np.array([[-4, 0, 2, -1, 0], [1, 3, -3, -1, 4], [2, 0, 1, 3, 0], [-2, 1, -3, -1, 5], [1, -5, 1, 0, 5]])
print("A =", A)

# A의 역행렬 계산
Ainv = inverseByAdjointMatrix(A)
print("A inverse =", Ainv)
