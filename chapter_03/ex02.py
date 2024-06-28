import numpy as np


# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("---", msg, "---")
    (n, m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i, j])
        print(line)
    print("")


A = np.array([[1., 2.], [3., 4.]])
B = np.array([[2., 2.], [1., 3.]])
C = np.array([[4., 5., 6.], [7., 8., 9.]])
v = np.array([[10.], [20.]])

pprint("A+B", A + B)  # 행렬의 합 A+B
pprint("A-B", A - B)  # 행렬의 차 A-B

pprint("3*A ", 3 * A)  # 행렬의 스칼라베 3A
pprint("2*v ", 2 * v)  # 행렬의 스칼라베 2v

pprint("matmul(A,B)", np.matmul(A, B))  # 행렬의 곱 AB
pprint("matmul(A,C)", np.matmul(A, C))  # 행렬의 곱 AC
pprint("A*v", A * v)  # 행렬과 벡터의 곱 Av

pprint("matrix_power(A, 2)", np.linalg.matrix_power(A, 2))
pprint("matrix_power(A, 3)", np.linalg.matrix_power(A, 3))

pprint("A*B", A * B)  # 행렬의 성분별 곱셉 A*B
pprint("A/B", A * B)  # 행렬의 성분별 나눗셈 A/B
pprint("A**2 == A*A", A ** 2)  # 행렬의 성분별 거듭제곱 A**2

pprint("A.T", A.T)  # 행렬의 전치 AT
pprint("v.T", v.T)  # 벡터의 전치 vT

M = np.diag([1, 2, 3])  # 대각행렬 diag(1,2,3) 생성
pprint("diag(1,2,3) =", M)

D11 = np.array([[1, 2], [3, 4]])
D12 = np.array([[5], [6]])
D21 = np.array([[7, 7]])
D22 = np.array([[8]])
D = np.block([[D11, D12], [D21, D22]])  # 블록행렬
pprint("blck matrix", D)
