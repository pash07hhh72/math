import numpy as np
p = np.array([0.3, 0.2, 0.5])


def scalar_product(vec_1: np.ndarray, vec_2: np.ndarray, p: np.ndarray = p) -> float:
    """

    :param vec_1: Вектор №1
    :param vec_2: Вектор №2
    :param p: Вектор вероятности
    :return: Скалярное произведение в деформированном пространстве
    """
    if vec_1.size != vec_2.size != p.size:
        raise ValueError("не совпадают размерности")

    return np.sum(vec_1 * vec_2 * p)


def E(X: np.ndarray, p: np.ndarray = p):
    """

    :param X: Вектор образов случ величины
    :param p: Вектор вероятности
    :return: Мат ожидание
    """
    return p.T @ X


def D(X: np.ndarray, p: np.ndarray = p):
    """

    :param X: Вектор образов случ величины
    :param p: Вектор вероятности
    :return: Дисперсия
    """
    e = E(X)
    return scalar_product(X - e, X - e, p)



print("hello.py")