import numpy as np


def invert_matrix_with_changed_column(A, A_inv, x, i):
    n = A.shape[0]

    # Шаг 1: Вычисляем l = A_inv * x
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


def input_matrix():
    # Ввод размерности квадратной матрицы A
    n = int(input("Введите размерность квадратной матрицы A: "))
    if n <= 0:
        print("Размерность квадратной матрицы должна быть положительным числом.")
        exit()

    # Ввод элементов матрицы A
    A = np.empty((n, n))
    for i in range(n):
        row = input(f"Введите строку {i + 1} матрицы A через пробел: ").split()
        if len(row) != n:
            print(f"Количество элементов в строке {i + 1} должно быть равно {n}.")
            exit()
        try:
            A[i] = list(map(float, row))
        except ValueError:
            print("Элементы матрицы должны быть числами.")
            exit()

    # Проверка на невырожденность матрицы A
    if np.linalg.det(A) == 0:
        print("Матрица A является вырожденной (сингулярной). Обратная матрица не может быть вычислена.")
        exit()

    # Обратная матрица к A
    A_inv = np.linalg.inv(A)

    # Ввод вектора x
    x = input(f"Введите вектор x высоты {n} через пробел: ").split()
    if len(x) != n:
        print(f"Размерность вектора x должна быть равна {n}.")
        exit()
    try:
        x = np.array(list(map(float, x)))
    except ValueError:
        print("Элементы вектора x должны быть числами.")
        exit()

    i = int(input("Введите номер столбца, который нужно заменить на вектор x: ")) - 1
    if not 0 <= i < n:
        print("Номер столбца должен быть корректным индексом столбца в матрице A.")
        exit()

    return A, A_inv, x, i