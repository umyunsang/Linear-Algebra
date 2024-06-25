#  다음과 같은 행렬과 벡터들 의 크기를 출력하는 프로그램을 작성하라.
#  A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  v = [1, 2, 3](열)
#  W = [1, 2, 3] (행)
#  B =[[1, 2, 3], [4, 5, 6]]

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([[1], [2], [3]])

print("A =", A)
print("V =", v)

print("A.shape =", A.shape)
print("v.shape =", v.shape)

w = np.array([1, 2, 3])
print("w =", w)
print("w.shape =", w.shape)