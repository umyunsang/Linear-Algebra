import numpy as np


# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("---", msg, "---")
    (n, m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:2f}".format(A[i, j]) + "\t"
        print(line)
    print("")


# LU 분해 함수
def LU(A):
    (n, m) = A.shape
    L = np.zeros((n, n))  # 행렬 L 초기화
    U = np.zeros((n, n))  # 행렬 U 초기화

    # 행렬 L과 U 계산
    # [수업자료 04.역행렬] 정리 4-10) LU 분해의 하삼각행렬과 상삼각행렬
    for i in range(0, n):
        for j in range(i, n):       # i<=j일 때,
            U[i, j] = A[i, j]       # U[i,j]에 A[i,j]의 요소를 할당
            for k in range(0, i):   # U[i,j]=A[i,j]-시그마(k=1부터 i-1까지)L[i,k]*U[k,i]
                U[i, j] = U[i, j] - L[i, k] * U[k, j]   # A[i,j] = U[i,j] 이므로 이 식이 성립
        L[i, i] = 1                       # L의 주 대각 성분 1로 설정 (하삼각행렬의 특징)
        if i < n - 1:                     # i가 마지막 행이 아닐 때
            p = i + 1                     # i>j를 표현하기 위한 방법
            for j in range(0, p):         # i>j일 때,
                L[p, j] = A[p, j]         # L[i,j]에 A[i,j]의 요소를 할당
                for k in range(0, j):     # L[i,j]=(A[i,j]-시그마(k=1부터 i-1까지)L[i,k]*U[k,j])/U[j,j]
                    L[p, j] = L[p, j] - L[p, k] * U[k, j]   # A[i,j] = L[i,j] 이므로 이 식이 성립
                    L[p, j] = L[p, j] / U[j, j]
    return L, U


# LU 분해를 이용한 Ax=b의 해 구하기
def LUSolver(A, b):
    L, U = LU(A)
    n = len(L)  # L의 크기를 구함
    # Ly=b 계산
    y = np.zeros((n, 1))            # L의 크기를 가진 열벡터 y 생성 (요소 값은 0)
    for i in range(0, n):           # 전방 대입법
        y[i] = b[i]                 # y의 i번째 요소에 b의 i번째 요소를 할당  
        for k in range(0, i):       # L은 하삼각 행렬이므로 y의 각 성분 y[i] =
            y[i] -= y[k] * L[i, k]  # b[i]-시그마(k=0부터 i-1까지)L[i,k]*y[k]
                                    # b[i] = y[i] 이므로 식이 성립

    # Ux=y 계산
    x = np.zeros((n, 1))               # L의 크기를 가진 열벡터 x 생성 (요소 값은 0)
    for i in range(n - 1, -1, -1):     # 후방 대입법
        x[i] = y[i]                    # x의 i번째 요소에 y의 i번째 요소를 할당
        if i < n - 1:                  # U는 상삼각 행렬이므로 x의 각 성분 x[i] =
            for k in range(i + 1, n):  # (y[i]-시그마(k=i+1부터 n-1까지)U[i,k]*x[k])/U[i,i]
                x[i] -= x[k] * U[i, k] # y[i] = x[i] 이므로 식이 성립
        x[i] = x[i] / float(U[i, i])   # 계산 편의를 위해 시그마연산 이후 U[i,i] 나누기
    return x


A = np.array([[5, 3, 2, 1], [6, 2, 4, 5], [7, 4, 1, 3], [4, 3, 5, 2]])
b = np.array([[4], [2], [5], [1]])

# 행렬 A의 LU 분해
L, U = LU(A)
pprint("A", A)
pprint("L", L)
pprint("U", U)

# LU 분해를 이용한 Ax=b의 해 구하기
x = LUSolver(A, b)
pprint("x", x)
