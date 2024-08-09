import numpy as np  # NumPy 라이브러리 임포트

def getVector(mag, deg):
    vec = np.zeros(2)  # 2차원 벡터 초기화
    # 방향을 라디안으로 변환 후 벡터의 x와 y 성분 계산
    vec[0] = mag * np.cos(deg * 2 * np.pi / 360)
    vec[1] = mag * np.sin(deg * 2 * np.pi / 360)
    return vec

def getMagDeg(vec):
    mag = np.sqrt(vec[0] * vec[0] + vec[1] * vec[1])  # 벡터의 크기 계산
    deg = np.arctan2(vec[1], vec[0]) * 360 / (2 * np.pi)  # 벡터의 방향 계산
    return mag, deg

# 벡터 생성 및 연산
F1 = getVector(100, 30)  # 크기 100N, 방향 30도인 벡터
F2 = getVector(120, 60)  # 크기 120N, 방향 60도인 벡터
Fsum = F1 + F2  # 두 벡터의 합
magn, angle = getMagDeg(Fsum)  # 합 벡터의 크기와 방향 계산

# 결과 출력
print("결합한 힘의 크기 : ", magn)
print("결합한 힘의 방향 : ", angle)
