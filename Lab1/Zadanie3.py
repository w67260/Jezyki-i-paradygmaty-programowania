from functools import reduce

def schedule_tasks_procedural(tasks):
    tasks.sort(key=lambda x: x[0])
    total_waiting_time = 0
    cumulative_time = 0
    optimal_order = []

    for execution_time, reward in tasks:
        cumulative_time += execution_time
        total_waiting_time += cumulative_time
        optimal_order.append((execution_time, reward))

    return optimal_order, total_waiting_time



def schedule_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[0])
    total_waiting_time, _ = reduce(
        lambda acc, task: (acc[0] + acc[1] + task[0], acc[1] + task[0]),
        sorted_tasks,
        (0, 0)
    )

    return sorted_tasks, total_waiting_time


tasks = [(3, 50), (1, 20), (2, 30), (4, 10)]


optimal_order, total_waiting_time = schedule_tasks_procedural(tasks)
print("Proceduralnie:")
print("Optymalna kolejność zadań:", optimal_order)
print("Całkowity czas oczekiwania:", total_waiting_time)


optimal_order, total_waiting_time = schedule_tasks_functional(tasks)
print("\nFunkcyjnie:")
print("Optymalna kolejność zadań:", optimal_order)
print("Całkowity czas oczekiwania:", total_waiting_time)