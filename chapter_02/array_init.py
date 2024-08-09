import numpy as np  # NumPy 라이브러리 임포트

# 2x3 크기의 모든 요소가 0인 배열 생성
a = np.zeros((2, 3))
print("a =")
print(a)  # 배열 a 출력

# 2x2 크기의 모든 요소가 1인 배열 생성
b = np.ones((2, 2))
print("b =")
print(b)  # 배열 b 출력

# 3x2 크기의 모든 요소가 3인 배열 생성
c = np.full((3, 2), 3)
print("c =")
print(c)  # 배열 c 출력

# 2x2 크기의 단위 행렬 생성
d = np.eye(2)
print("d =")
print(d)  # 배열 d 출력
