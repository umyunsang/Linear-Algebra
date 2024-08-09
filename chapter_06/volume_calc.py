import numpy as np  # NumPy 라이브러리 임포트


def tripleProduct(u, v, w):
    """
    벡터 u, v, w로 정의된 평행육면체의 부피를 계산합니다.
    """
    M = np.zeros((3, 3))  # 3x3 행렬 M 초기화
    M[0] = u  # 첫 번째 행에 벡터 u 할당
    M[1] = v  # 두 번째 행에 벡터 v 할당
    M[2] = w  # 세 번째 행에 벡터 w 할당
    val = np.linalg.det(M)  # 행렬 M의 행렬식 계산
    return val


# 벡터 A, B, C, D 정의
A = np.array([1, 2, 3])
B = np.array([0, 5, 2])
C = np.array([2, 2, 4])
D = np.array([2, 4, 1])

# 벡터 u, v, w 계산
u = B - A
v = C - A
w = D - A

# tripleProduct 함수 호출 및 부피 계산
val = tripleProduct(u, v, w)
print("부피 : ", np.absolute(val))  # 절댓값으로 부피 출력
