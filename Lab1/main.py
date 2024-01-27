import numpy as np

# А - квадратная матрица, A_inv - матрица, обратная матрице А
def invert_matrix_with_changed_column(A, A_inv, x, i):
    # Вернем размерность квадратной матрицы
    n = A.shape[0]

    # Шаг 1: Вычислим l = A_inv * x
    l = np.dot(A_inv, x)

    # Проверяем, равен ли l_i нулю
    if abs(l[i]) < 1e-10:
        print("Матрица C необратима.")
        return None

    # Шаг 2: Формируем вектор ~l
    l_tilde = l.copy()
    l_tilde[i] = -1

    # Шаг 3: Находим ^l
    l_hat = -(1 / l[i]) * l_tilde

    # Шаг 4: Формируем матрицу Q
    Q = np.eye(n)
    Q[:, i] = l_hat

    # Шаг 5: Находим D = Q * A_inv
    D = np.dot(Q, A_inv)

    return D


if __name__ == "__main__":
    # Ввод матрицы A
    n = int(input("Введите размерность квадратной матрицы A: "))
    A = np.empty((n, n))
    for i in range(n):
        A[i] = list(map(float, input(f"Введите строку {i + 1} матрицы A через пробел: ").split()))

    # Обратная матрица к A
    B = np.linalg.inv(A)

    # Ввод вектора x
    x = np.array(list(map(float, input(f"Введите вектор x высоты {n} через пробел: ").split())))

    # Номер столбца для замены
    i = int(input("Введите номер столбца, который нужно заменить на вектор x: ")) - 1

    D = invert_matrix_with_changed_column(A, B, x, i)
    if D is not None:
        print("Обратная матрица к C:")
        print(D)
