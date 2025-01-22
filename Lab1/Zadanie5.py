from functools import reduce


def schedule_tasks_procedural(tasks):
    tasks = sorted(tasks, key=lambda x: x[1])

    selected_tasks = []
    max_reward = 0
    last_end_time = 0

    for task in tasks:
        start, end, reward = task
        if start >= last_end_time:
            selected_tasks.append(task)
            max_reward += reward
            last_end_time = end

    return max_reward, selected_tasks



def schedule_tasks_functional(tasks):
    tasks = sorted(tasks, key=lambda x: x[1])

    def reducer(acc, task):
        selected_tasks, max_reward, last_end_time = acc
        start, end, reward = task

        if start >= last_end_time:
            return selected_tasks + [task], max_reward + reward, end
        return selected_tasks, max_reward, last_end_time

    selected_tasks, max_reward, _ = reduce(reducer, tasks, ([], 0, 0))
    return max_reward, selected_tasks



tasks = [(1, 3, 50), (2, 5, 20), (4, 6, 70), (6, 7, 60), (5, 8, 30)]

max_reward, selected_tasks = schedule_tasks_procedural(tasks)
print("Proceduralnie:")
print("Maksymalna nagroda:", max_reward)
print("Lista zadań:", selected_tasks)

max_reward, selected_tasks = schedule_tasks_functional(tasks)
print("\nFunkcyjnie:")
print("Maksymalna nagroda:", max_reward)
print("Lista zadań:", selected_tasks)