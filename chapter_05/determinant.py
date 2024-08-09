import numpy as np  # NumPy 라이브러리 임포트

# 행렬 A의 i행과 j열을 제거하고 생성된 행렬을 반환하는 함수
def getMinorMatrix(A, i, j):
    n = len(A)  # A의 크기 (행렬의 차원)
    M = np.zeros((n - 1, n - 1))  # 새로운 행렬 M을 0으로 초기화

    # 행렬 A의 i행과 j열을 제거하여 M을 생성
    for a in range(n - 1):
        k = a if a < i else a + 1  # i행을 제거하기 위해 인덱스 조정
        for b in range(n - 1):
            l = b if b < j else b + 1  # j열을 제거하기 위해 인덱스 조정
            M[a, b] = A[k, l]  # M의 요소를 A의 해당 요소로 설정
    return M

# 행렬 M의 행렬식을 계산하는 함수
def determinant(M):
    if len(M) == 2:  # 2x2 행렬의 경우 직접 계산
        return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]

    detVal = 0
    # 모든 열에 대해 Laplace 전개를 이용한 행렬식 계산
    for c in range(len(M)):
        # Minor 행렬을 구하고 재귀적으로 행렬식 계산
        detVal += ((-1) ** c) * M[0, c] * determinant(getMinorMatrix(M, 0, c))
    return detVal

# 예제 행렬 A 정의
A = np.array([[-4, 0, 2, -1, 0], [1, 3, -3, -1, 4], [2, 0, 1, 3, 0], [-2, 1, -3, -1, 5], [1, -5, 1, 0, 5]])

# 행렬 A와 A의 행렬식 출력
print("A =", A)
print("det(A) =", determinant(A))
