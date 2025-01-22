from functools import reduce
import numpy as np

def matrix_operation(matrix_list, operation):
    if not matrix_list:
        return "Błąd: Lista macierzy jest pusta."

    def apply_operation(a, b, operation):
        try:
            if operation == "add":
                return a + b
            elif operation == "multiply":
                return np.dot(a, b)
            else:
                return f"Błąd: Nieznana operacja '{operation}'."
        except Exception as e:
            return f"Błąd w operacji: {e}"

    try:
        result = reduce(lambda a, b: apply_operation(a, b, operation), matrix_list)
    except Exception as e:
        return f"Błąd podczas łączenia macierzy: {e}"

    return result




matrices = [
    np.array([[1, 2], [3, 4]]),
    np.array([[5, 6], [7, 8]]),
    np.array([[9, 10], [11, 12]])
]

operation = "add"
result = matrix_operation(matrices, operation)
if isinstance(result, str):
    print(result)
else:
    print("Wynik sumowania macierzy:")
    print(result)

operation = "multiply"
result = matrix_operation(matrices, operation)
if isinstance(result, str):
    print(result)
else:
    print("\nWynik mnożenia macierzy:")
    print(result)