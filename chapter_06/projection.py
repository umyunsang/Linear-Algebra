import numpy as np  # NumPy 라이브러리 임포트

def angle2vectors(v, w):
    """
    두 벡터 v와 w 사이의 사잇각을 계산합니다.
    """
    vnorm = np.linalg.norm(v)  # 벡터 v의 크기 계산
    wnorm = np.linalg.norm(w)  # 벡터 w의 크기 계산
    vwdot = np.dot(v.T, w)  # 벡터 v와 w의 내적 계산
    angle = np.arctan(vwdot / (vnorm * wnorm)) * 360 / np.pi  # 사잇각 계산 (도 단위)
    return angle

def orthProj(u, x):
    """
    벡터 x를 벡터 u에 정사영합니다.
    """
    xu_dot = np.dot(x.T, u)  # 벡터 x와 u의 내적 계산
    uu_dot = np.dot(u.T, u)  # 벡터 u의 제곱 노름 계산
    projux = (xu_dot / uu_dot) * u  # 벡터 x의 u 위로의 정사영 계산
    return projux

# 예시 벡터
A = np.array([[2], [4], [1]])
B = np.array([[1], [-1], [3]])

# 벡터 A와 B의 사잇각 계산
angle = angle2vectors(A, B)

# 벡터 A의 B 위로의 정사영 계산
projAB = orthProj(B, A)

# 결과 출력
print("A와 B의 사잇각 : ", angle)
print("A의 B 위로의 정사영 : \n", projAB)
