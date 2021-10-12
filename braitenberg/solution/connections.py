from typing import Tuple

import numpy as np

k_x = 0.65
k_y = 0.5

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    (X,Y) = shape
    X_new = int(X*k_x)
    Y_new = int(Y*k_y)
    res[0:X_new,0:Y_new]=-0.1
    res[X_new:X,0:Y_new]=1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    (X,Y) = shape
    X_new = int(X*k_x)
    Y_new = int(Y*k_y)
    res[0:X_new,-Y_new::]=-0.1
    res[X_new:X,-Y_new::]=1
    return res
