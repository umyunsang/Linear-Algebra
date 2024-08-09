import numpy as np  # NumPy 라이브러리 임포트

print("벡터의 결합에 의한 행렬 생성")

# 벡터 정의
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

# np.vstack: 벡터를 행으로 결합하여 행렬 생성
A = np.vstack([v1, v2, v3])
print("A =", A)

# np.column_stack: 벡터를 열로 결합하여 행렬 생성
B = np.column_stack([v1, v2, v3])
print("B =", B)

# 직접 정의한 행렬 C
C = np.array([[1, 2], [3, 4], [5, 6]])
print("C =", C)

# np.column_stack: 행렬 C의 열에 벡터 v3을 추가하여 새로운 행렬 D 생성
D = np.column_stack([C, v3])
print("D =", D)

print("행렬의 성분 접근")

# 4x4 행렬 E 정의
E = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 특정 성분 접근
print("E[0,3] =", E[0, 3])  # 1행 4열의 성분
print("E[1,2] =", E[1, 2])  # 2행 3열의 성분

# 부분 행렬 접근
print("E[0:2, 2] =", E[0:2, 2])  # E의 1~2행의 3열에 해당하는 부분행렬
print("E[0:2, 2:4] =", E[0:2, 2:4])  # E의 1~2행의 3~4열에 해당하는 부분행렬
print("E[2, :] =", E[2, :])  # E의 3행에 해당하는 부분행렬

print("성분의 변경")

# 성분 변경 전 행렬 E 출력
print("E =", E)

# 성분 변경 및 확인
print("E[0,0] =", E[0, 0])
E[0, 0] = -1  # E의 1행 1열 성분을 -1로 변경
print(E)
print("E[0,0] =", E[0, 0])
