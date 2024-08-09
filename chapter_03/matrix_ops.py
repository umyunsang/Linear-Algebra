import numpy as np  # NumPy 라이브러리 임포트

# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("---", msg, "---")
    (n, m) = A.shape  # A의 행렬 크기 (n, m) 가져오기
    for i in range(n):
        line = ""
        for j in range(m):
            line += "{0:.2f}".format(A[i, j]) + " "  # 행렬 성분 포맷팅 및 문자열 생성
        print(line)
    print("")

# 행렬 및 벡터 정의
A = np.array([[1., 2.], [3., 4.]])
B = np.array([[2., 2.], [1., 3.]])
C = np.array([[4., 5., 6.], [7., 8., 9.]])
v = np.array([[10.], [20.]])

# 행렬 연산 수행 및 결과 출력
pprint("A+B", A + B)  # 행렬의 합 A+B
pprint("A-B", A - B)  # 행렬의 차 A-B

pprint("3*A", 3 * A)  # 행렬의 스칼라배 3A
pprint("2*v", 2 * v)  # 벡터의 스칼라배 2v

pprint("matmul(A,B)", np.matmul(A, B))  # 행렬의 곱 AB
pprint("matmul(A,C)", np.matmul(A, C))  # 행렬의 곱 AC

# 행렬과 벡터의 곱 연산
pprint("A*v", A @ v)  # 행렬 A와 벡터 v의 곱 (A*v)

# 행렬 거듭제곱
pprint("matrix_power(A, 2)", np.linalg.matrix_power(A, 2))  # A^2
pprint("matrix_power(A, 3)", np.linalg.matrix_power(A, 3))  # A^3

# 성분별 연산
pprint("A*B", A * B)  # 행렬의 성분별 곱셈 A*B
pprint("A/B", A / B)  # 행렬의 성분별 나눗셈 A/B
pprint("A**2 == A*A", A ** 2)  # 행렬의 성분별 거듭제곱 A**2

# 행렬의 전치
pprint("A.T", A.T)  # 행렬 A의 전치
pprint("v.T", v.T)  # 벡터 v의 전치

# 대각행렬 생성
M = np.diag([1, 2, 3])  # 대각행렬 diag(1,2,3) 생성
pprint("diag(1,2,3) =", M)

# 블록 행렬 생성
D11 = np.array([[1, 2], [3, 4]])
D12 = np.array([[5], [6]])
D21 = np.array([[7, 7]])
D22 = np.array([[8]])
D = np.block([[D11, D12], [D21, D22]])  # 블록 행렬 생성
pprint("block matrix", D)
