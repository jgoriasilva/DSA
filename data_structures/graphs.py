from typing import *
from queue import Queue


def create_graph() -> Dict[int, List[int]]:

    graph = {
        1: [2,3], 
        2: [4],
        3: [5],   
        4: [3],
        5: [],
        6: [5],
    }

    return graph


def create_graph_from_edges(edges: List[List[int]]) -> Dict[int, List[int]]:

    graph = {}

    for edge in edges:
        if len(edge) == 1:
            graph[edge[0]] = []
        else:
            node1, node2 = edge
            if node1 not in graph: graph[node1] = []
            if node2 not in graph: graph[node2] = []

            graph[node1].append(node2)
            graph[node2].append(node1)

    return graph


def dfs_iterative(graph: Dict[int, List[int]], source: int) -> None:
    res = []
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        res.append(current)
        for neighbor in graph[current]:
            stack.append(neighbor) 

    print(res)


def dfs_recursive(graph, source, res) -> None:
    res.append(source)

    for neighbor in graph[source]:
        dfs_recursive(graph, neighbor, res)
    
    return res



def bfs(graph: Dict[int, List[int]], source: int) -> None:
    res = []
    queue = Queue()
    queue.put(source)

    while not queue.empty():
        current = queue.get()
        res.append(current)

        for neighbor in graph[current]:
            queue.put(neighbor)

    print(res)


def has_path_recursive(graph, src, dst) -> bool:
    if src == dst: return True

    for neighbor in graph[src]:
        if has_path_recursive(graph, neighbor, dst):
            return True
    
    return False



def has_path_dfs(graph, src, dst) -> bool:

    stack = [src]

    while len(stack) > 0:
        current = stack.pop()
        if current == dst: return True
        for neighbor in graph[current]:
            stack.append(neighbor)

    return False


def has_path_bfs(graph, src, dst) -> bool:


    queue = Queue()
    queue.put(src)

    while not queue.empty():
        current = queue.get()
        if current == dst: return True
        for neighbor in graph[current]:
            queue.put(neighbor)

    return False

def undirected_has_path_dfs(graph: Dict[int, List[int]], src: int, dst: int, visited: Set[int]) -> bool:
    if src == dst: return True
    if src in visited: return False
    visited.add(src)

    for neighbor in graph[src]:
        if undirected_has_path_dfs(graph, neighbor, dst, visited): return True

    return False

def count_connected_components(graph: Dict[int, List[int]]) -> int:

    visited = set()
    count = 0

    def dfs(graph, src, visited):
        if src in visited: return False
        visited.add(src)

        for neighbor in graph[src]:
            dfs(graph, neighbor, visited)
        
        return True

    for node in list(graph.keys()):
        if dfs(graph, node, visited): count += 1

    return count



def largest_component(graph: Dict[int, List[int]]) -> int:

    max_size = 0
    visited = set()

    def dfs(graph, node, visited):
        if node in visited: return 0
        visited.add(node)
        size = 1

        for neighbor in graph[node]:
            size += dfs(graph, neighbor, visited)

        return size

    for node in list(graph.keys()):
        size = dfs(graph, node, visited)
        max_size = max(max_size, size)

    return max_size

def largest_component_bfs(graph: Dict[int, List[int]]) -> int:

    visited = set()
    max_size = 0


    for src in list(graph.keys()):

        queue = Queue()
        queue.put(src)
        size = 0

        while not queue.empty():
            current = queue.get()
            if current in visited: continue
            visited.add(current)
            size += 1

            for neighbor in graph[current]:
                queue.put(neighbor)

        max_size = max(max_size, size)

    return max_size

def shortest_path_bfs(graph: Dict[int, List[int]], src: int, dst: int) -> int:

    queue = Queue()
    queue.put((src, 0))
    visited = {src}

    while not queue.empty():
        current, l = queue.get()
        if current == dst: return l
        for neighbor in graph[current]:
            if neighbor in visited: continue
            queue.put((neighbor, l+1))
            visited.add(neighbor)

    return float('inf')



def shortest_path_dfs(graph: Dict[int, List[int]], src: int, dst: int) -> int:

    if src == dst: return 0

    min_l = 0
    visited = set()


    def dfs(graph, src, dst, visited):
        if src == dst: return 1
        if src in visited: return 0
        visited.add(src)

        l = 1

        for neighbor in graph[src]:
            l += dfs(graph, neighbor, dst, visited)
        
        return l

    for neighbor in graph[src]:
        l = dfs(graph, neighbor, dst, visited)
        min_l = min(min_l, l)


    return min_l

def main():

    graph = create_graph()

    # dfs_iterative(graph, 1)
    # bfs(graph, 1)

    # print(dfs_recursive(graph, 1, []))


    print(has_path_recursive(graph, 4, 1))
    print(has_path_dfs(graph, 1, 5))
    print(has_path_bfs(graph, 1, 5))

    # edges = [
    #     [1, 2],
    #     [1, 3],
    #     [2, 3],
    #     [2, 4],
    #     [3, 5],
    #     [6, 7],
    # ]


    edges = [
        [1, 2],
        [5, 4],
        [5, 6],
        [5, 7],
        [5, 8],
        [3],
    ]


    graph = create_graph_from_edges(edges)

    print(undirected_has_path_dfs(graph, 1, 6, set()))

    print(count_connected_components(graph))

    print(largest_component(graph))
    print(largest_component_bfs(graph))

    print(shortest_path_bfs(graph, 1, 2))

    return


if __name__ == '__main__':
    main()