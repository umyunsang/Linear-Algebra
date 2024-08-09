import numpy as np  # NumPy 라이브러리 임포트

# 행렬을 예쁘게 출력하는 함수
def pprint(msg, A):
    """
    주어진 행렬 A를 예쁘게 출력하는 함수
    """
    print("---", msg, "---")
    (n, m) = A.shape
    for i in range(n):
        line = ""
        for j in range(m):
            line += "{0:2f}".format(A[i, j]) + "\t"
        print(line)
    print("")

# 가우스 소거법 함수
def gauss(A):
    """
    가우스 소거법을 사용하여 선형 방정식 시스템을 푸는 함수
    """
    (n, m) = A.shape

    for i in range(min(n, m)):
        # i번째 열에서 절댓값이 최대인 성분의 행 선택
        maxEl = abs(A[i, i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > maxEl:
                maxEl = abs(A[k, i])
                maxRow = k

        # 현재 i번째 행과 최댓값을 갖는 행 maxRow의 교환
        A[[i, maxRow], :] = A[[maxRow, i], :]

        # 추축성분을 1로 만들기
        piv = A[i, i]
        A[i, :] = A[i, :] / piv

        # 현재 i번째 열의 i번째 행을 제외한 모두 성분을 0으로 만들기
        for k in range(n):
            if k != i:
                c = A[k, i] / A[i, i]
                A[k, i:] = A[k, i:] - c * A[i, i:]

        pprint(str(i + 1) + "번째 반복", A) # 중간 과정 출력

    # Ax=b의 해 반환
    x = np.zeros(m - 1)
    for i in range(m - 1):
        x[i] = A[i, m - 1]
    return x

# 주어진 행렬 A 정의
A = np.array([[2., 2., 4., 18.],
              [1., 3., 2., 13.],
              [3., 1., 3., 14.]])

pprint("주어진 문제", A)  # 주어진 행렬 출력
x = gauss(A)  # 가우스 소거법을 사용하여 해 계산

# 해 출력
(n, m) = A.shape
line = "해:\t"
for i in range(m - 1):
    line += "{0:.2f}".format(x[i]) + "\t"
print(line)
