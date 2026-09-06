import numpy as np
from typing import List, Callable



def diff(vec: np.ndarray, functions: List[Callable], h: float = 0.001) -> np.ndarray:
    """
    f: R**n -> R**m

    :param h: константа приращения, для вычисления частной производной
    :param vec: вычисляем производную в точке vec (размерность n)
    :param functions: набор функция, где индекс функции в списке соответствует номеру координаты вектора образа
    :return: Matrix_n*m матрица Якоби
    """
    result = np.zeros(vec.size * len(functions))
    result = result.reshape(len(functions), vec.size)
    for i in range(len(functions)):
        func = functions[i]
        for num in range(0, vec.size):
            new_vec = np.zeros(vec.size)
            new_vec[num] = h
            df_dx = (func(vec + new_vec) - func(vec)) / h
            result[i][num] = df_dx
    return result


def f_1(arr: np.ndarray):
    x = arr[0]
    y = arr[1]
    z = arr[2]
    return x ** 2 + 2 * x * y + z

def f_2(arr: np.ndarray):
    x = arr[0]
    y = arr[1]
    z = arr[2]
    return x * y

def f_3(arr: np.ndarray):
    x = arr[0]
    y = arr[1]
    z = arr[2]
    return 30 * z


vec = np.array([1, 3, 1])
print(diff(vec, [f_1, f_2, f_3]))

vec_1 = np.array([1, 2, 3])
vec_2 = np.array([0, 0, 7])
vec_3 = np.array([1, 4, 10])

y = np.array([1, 2, 3])

