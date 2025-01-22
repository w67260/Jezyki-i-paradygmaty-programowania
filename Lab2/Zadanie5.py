import ast
import inspect

def validate_code(code: str):
    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        print(f"Błąd składni: {e}")
        return False

def generate_code(template: str, variables: dict):
    try:
        code = template.format(**variables)
        if validate_code(code):
            return code
        else:
            return None
    except KeyError as e:
        print(f"Brakuje zmiennej w szablonie: {e}")
        return None


def execute_code(code: str):
    try:
        exec(code, globals())
    except Exception as e:
        print(f"Błąd podczas wykonywania kodu: {e}")




template = """
def add_numbers(x, y):
    return x + y + {extra_value}
"""

variables = {"extra_value": 5}

generated_code = generate_code(template, variables)

if generated_code:
    print("Wygenerowany kod:")
    print(generated_code)
    execute_code(generated_code)
    add_numbers_result = add_numbers(3, 4)
    print(f"Rezultat dodawania: {add_numbers_result}")
else:
    print("Wygenerowanie kodu nie powiodło się.")