import numpy as np

def validate_matrices(matrix_a, matrix_b=None, operation=None):
    if operation == "add":
        if matrix_a.shape != matrix_b.shape:
            print("Błąd: Dodawanie wymaga macierzy o tych samych wymiarach.")
            return False
    elif operation == "multiply":
        if matrix_a.shape[1] != matrix_b.shape[0]:
            print("Błąd: Mnożenie wymaga, aby liczba kolumn pierwszej macierzy równała się liczbie wierszy drugiej macierzy.")
            return False
    elif operation == "transpose":
        return True
    else:
        print(f"Błąd: Nieznana operacja '{operation}'.")
        return False

    return True

def execute_matrix_operation(operation_string):
        local_vars = {}
        exec(operation_string, {"np": np}, local_vars)

        matrix_a = local_vars.get("matrix_a")
        matrix_b = local_vars.get("matrix_b", None)
        operation = local_vars.get("operation")
        result = None

        if operation == "add":
            validate_matrices(matrix_a, matrix_b, operation)
            result = matrix_a + matrix_b
        elif operation == "multiply":
            validate_matrices(matrix_a, matrix_b, operation)
            result = np.dot(matrix_a, matrix_b)
        elif operation == "transpose":
            validate_matrices(matrix_a, operation=operation)
            result = matrix_a.T
        else:
            raise ValueError(f"Operacja '{operation}' jest nieobsługiwana.")

        return result

operation_script = """
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])
operation = "multiply"
"""


result = execute_matrix_operation(operation_script)
print("Wynik operacji:")
print(result)