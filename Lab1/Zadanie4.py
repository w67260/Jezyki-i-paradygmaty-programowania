def knapsack_procedural(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    return dp[n][capacity], selected_items



def knapsack_functional(items, capacity):
    n = len(items)

    def knapsack(index, remaining_capacity, memo):
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]

        if index == n or remaining_capacity == 0:
            return 0, []

        value, weight = items[index]

        exclude_value, exclude_items = knapsack(index + 1, remaining_capacity, memo)

        if weight <= remaining_capacity:
            include_value, include_items = knapsack(index + 1, remaining_capacity - weight, memo)
            include_value += value
        else:
            include_value, include_items = 0, []

        if include_value > exclude_value:
            result = include_value, [(value, weight)] + include_items
        else:
            result = exclude_value, exclude_items

        memo[(index, remaining_capacity)] = result
        return result

    return knapsack(0, capacity, {})



items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

max_value, selected_items = knapsack_procedural(items, capacity)
print("Proceduralnie:")
print("Maksymalna wartość:", max_value)
print("Lista wybranych przedmiotów:", selected_items)

max_value, selected_items = knapsack_functional(items, capacity)
print("Funkcyjnie:")
print("Maksymalna wartość:", max_value)
print("Lista wybranych przedmiotów:", selected_items)