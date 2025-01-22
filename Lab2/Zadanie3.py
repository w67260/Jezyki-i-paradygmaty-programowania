def analyze_heterogeneous_data(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    max_number = max(numbers) if numbers else None

    strings = list(filter(lambda x: isinstance(x, str), data))
    longest_string = max(strings, key=len) if strings else None

    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    largest_tuple = max(tuples, key=len) if tuples else None

    return {
        "max_number": max_number,
        "longest_string": longest_string,
        "largest_tuple": largest_tuple
    }



heterogeneous_data = [
    42, "hello", (1, 2, 3), 3.14, "world", (10, 20), 100, "Python", (1,), {}, []
]

results = analyze_heterogeneous_data(heterogeneous_data)

print("Największa liczba:", results["max_number"])
print("Najdłuższy napis:", results["longest_string"])
print("Krotka o największej liczbie elementów:", results["largest_tuple"])