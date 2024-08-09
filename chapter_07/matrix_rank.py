import numpy as np  # NumPy 라이브러리 임포트


def pprint(msg, A):
    print("---", msg, "---")
    (n, m) = A.shape
    for i in range(n):
        line = ""
        for j in range(m):
            line += "{0:.2f}".format(A[i, j]) + "\t"  # 행렬의 성분을 소수점 두 자리까지 포맷
        print(line)
    print("")


# 단위 행렬 4x4 생성 및 출력
A = np.eye(4)
pprint("A", A)
print("rank(A) =", np.linalg.matrix_rank(A))  # 행렬 A의 랭크 출력

# 3x3 제로 행렬 생성 및 출력
B = np.zeros((3, 3))
pprint("B", B)
print("rank(B) =", np.linalg.matrix_rank(B))  # 행렬 B의 랭크 출력

# 4x5 행렬 C 생성 및 출력
C = np.array([[2, 5, -3, -4, 8], [4, 7, -4, -3, 9], [6, 9, -5, 2, 4], [0, -9, 6, 5, -6]])
pprint("C", C)
print("rank(C) =", np.linalg.matrix_rank(C))  # 행렬 C의 랭크 출력

# 행렬 C의 전치 행렬 생성 및 출력
CT = np.transpose(C)
pprint("C^T", CT)
print("rank(C^T) =", np.linalg.matrix_rank(CT))  # 행렬 C^T의 랭크 출력
