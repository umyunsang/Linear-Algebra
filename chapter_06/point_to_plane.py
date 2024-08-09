import numpy as np  # NumPy 라이브러리 임포트


def distPt2Pl(A, W, P):
    """
    점 P와 평면을 정의하는 점 A 및 법선 벡터 W 사이의 거리 계산.

    :param A: 평면 위의 점 (numpy 배열)
    :param W: 평면의 법선 벡터 (numpy 배열)
    :param P: 거리 측정 대상 점 (numpy 배열)
    :return: 점 P와 평면 사이의 거리
    """
    num = np.dot((P - A).T, W)  # 점 P에서 평면 A까지의 벡터와 법선 벡터 W의 내적
    deno = np.linalg.norm(W)  # 법선 벡터 W의 노름 (길이)
    val = np.absolute(num) / deno  # 거리 계산: 내적의 절댓값을 법선 벡터의 노름으로 나눔
    return val


# 점 A, 법선 벡터 W, 점 P 정의
A = np.array([2, 3, 4])
W = np.array([1, 2, 3])
P = np.array([0, 1, 2])

# 거리 계산 및 출력
print("거리 : ", distPt2Pl(A, W, P))
