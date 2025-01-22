def divide_packages(package_weights, max_weight):
    package_weights.sort(reverse=True)
    trips = []

    for weight in package_weights:
        placed = False
        for trip in trips:
            if sum(trip) + weight <= max_weight:
                trip.append(weight)
                placed = True
                break

        if not placed:
            trips.append([weight])


    return len(trips), trips




package_weights = [5, 10, 7, 8, 2, 4]
max_weight = 15

num_trips, trip_packages = divide_packages(package_weights, max_weight)

print(f"Minimalna liczba kursów: {num_trips}")
print("Paczek w każdym kursie:")
for i, trip in enumerate(trip_packages, start=1):
    print(f"Kurs {i}: {trip}")