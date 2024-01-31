from function import input_matrix, invert_matrix_with_changed_column

if __name__ == "__main__":
    A, A_inv, x, i = input_matrix()

    B_inv = invert_matrix_with_changed_column(A, A_inv, x, i)

    if B_inv is not None:
        print("Обратная матрица к C:")
        print(B_inv)
