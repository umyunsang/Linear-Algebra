#  다음과 같은 행렬 A와 벡터 v를 파이썬으로 정의하고,
# 이를 출력하는 프로그램을 작성하라.
#  A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# v = [1, 2, 3]

import numpy as np  # NumPy 라이브러리 임포트

# 행렬 A 정의
A = np.array([[1, 2, 3],  # 첫 번째 행
              [4, 5, 6],  # 두 번째 행
              [7, 8, 9]]) # 세 번째 행

# 벡터 v 정의 (열 벡터 형태)
v = np.array([[1],  # 첫 번째 원소
              [2],  # 두 번째 원소
              [3]]) # 세 번째 원소

# 행렬 A 출력
print("A =")
print(A)

# 벡터 v 출력
print("V =")
print(v)
