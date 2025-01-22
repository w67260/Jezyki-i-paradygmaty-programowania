from functools import reduce
from collections import deque


def bfs_shortest_path(graph, start, end):
    def bfs(queue, visited, paths):
        if not queue:
            return []

        current, path = queue.popleft()

        if current == end:
            return path

        neighbors = filter(lambda neighbor: neighbor not in visited, graph.get(current, []))

        updated_queue = reduce(
            lambda acc, neighbor: acc + deque([(neighbor, path + [neighbor])]),
            neighbors,
            queue
        )

        updated_visited = visited | {current}

        return bfs(deque(updated_queue), updated_visited, paths)

    return bfs(deque([(start, [start])]), set(), {})



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'

shortest_path = bfs_shortest_path(graph, start, end)
print(f"Najkrótsza ścieżka z {start} do {end}: {shortest_path}")