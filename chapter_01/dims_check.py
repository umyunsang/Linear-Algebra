#  다음과 같은 행렬과 벡터들 의 크기를 출력하는 프로그램을 작성하라.
#  A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  v = [1, 2, 3](열)
#  W = [1, 2, 3] (행)
#  B =[[1, 2, 3], [4, 5, 6]]

import numpy as np  # NumPy 라이브러리 임포트

# 행렬 A 정의
A = np.array([[1, 2, 3],  # 첫 번째 행
              [4, 5, 6],  # 두 번째 행
              [7, 8, 9]]) # 세 번째 행

# 열 벡터 v 정의
v = np.array([[1],  # 첫 번째 원소
              [2],  # 두 번째 원소
              [3]]) # 세 번째 원소

# 행렬 A와 열 벡터 v 출력
print("A =")
print(A)

print("V =")
print(v)

# 행렬 A와 열 벡터 v의 크기 출력
print("A.shape =", A.shape)  # A의 크기 출력 (행, 열)
print("v.shape =", v.shape)  # v의 크기 출력 (행, 열)

# 행 벡터 w 정의
w = np.array([1, 2, 3])  # 한 행의 3개 원소를 가진 벡터

# 행 벡터 w 출력 및 크기 출력
print("w =", w)
print("w.shape =", w.shape)  # w의 크기 출력 (원소의 개수,)

# 행렬 B 정의
B = np.array([[1, 2, 3],  # 첫 번째 행
              [4, 5, 6]]) # 두 번째 행

# 행렬 B의 크기 출력
print("B =", B)
print("B.shape =", B.shape)  # B의 크기 출력 (행, 열)
