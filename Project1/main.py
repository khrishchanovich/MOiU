from function import input_matrix, invert_matrix_with_changed_column

if __name__ == "__main__":
    A, A_inv, x, i = input_matrix()

    D = invert_matrix_with_changed_column(A, A_inv, x, i)

    if D is not None:
        print("Обратная матрица к C:")
        print(D)
