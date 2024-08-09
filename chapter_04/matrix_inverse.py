import numpy as np  # NumPy 라이브러리 임포트


# 행렬을 보기 좋게 출력하는 함수
def pprint(msg, A):
    print("---", msg, "---")
    (n, m) = A.shape  # A의 행과 열의 크기 가져오기
    for i in range(n):
        line = ""
        for j in range(m):
            line += "{0:2f}".format(A[i, j]) + "\t"  # 행렬의 각 성분을 포맷하여 문자열 생성
        print(line)
    print("")


# 행렬 A 정의 및 출력
A = np.array([[1., 2.], [3., 4.]])
pprint("A", A)

# 행렬 A의 역행렬을 계산
Ainv1 = np.linalg.matrix_power(A, -1)  # matrix_power()를 사용한 역행렬 계산
pprint("linalg.matrix_power(A, -1) => Ainv1", Ainv1)

Ainv2 = np.linalg.inv(A)  # inv()를 사용한 역행렬 A^-1 계산
pprint("np.linalg.inv(A) => Ainv2", Ainv2)

# 행렬 A와 역행렬 A^-1의 곱 계산
pprint("A*Ainv1", np.matmul(A, Ainv1))  # A와 Ainv1의 곱
pprint("A*Ainv2", np.matmul(A, Ainv2))  # A와 Ainv2의 곱

# 난수를 이용한 3x3 행렬 B 생성 및 출력
B = np.random.rand(3, 3)  # 난수로 3x3 행렬 B 생성
pprint("B", B)

# 행렬 B의 역행렬 계산
Binv = np.linalg.inv(B)  # B의 역행렬 B^-1 계산
pprint("Binv =", Binv)

# 행렬 B와 역행렬 B^-1의 곱 계산
pprint("B*Binv =", np.matmul(B, Binv))  # B와 Binv의 곱

# 선형 시스템 Cx = D의 해 계산
C = np.array([[5, 3, 2, 1], [6, 2, 4, 5], [7, 4, 1, 3], [4, 3, 5, 2]])  # 계수 행렬 C
D = np.array([[4], [2], [5], [1]])  # 결과 벡터 D
x = np.matmul(np.linalg.inv(C), D)  # 해 x 계산
pprint("x", x)  # 해 x 출력
pprint("C*x", np.matmul(C, x))  # C*x의 결과가 D와 일치하는지 확인
