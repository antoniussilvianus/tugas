# Created By : Anton
# Created Date : 18-01-2024
import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        priority_queue = [(0, start)]
        visited = set()
        distances = {node: float("inf") for node in self.graph}

        distances[start] = 0

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(priority_queue, (new_dist, neighbor))

        print("Shortest distances from", start + ":")
        for node in visited:
            print(f"{node}: {distances[node]}")


# Example usage:
graph = Graph()
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 1)

graph.dijkstra("A")