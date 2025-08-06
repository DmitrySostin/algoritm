"""Module providing a function printing python version."""
from collections import deque


class DirectedGraph:
    """ Graph """
    def __init__(self):
        self.graph = {}

    def add_vertex(self, u, v):
        """ Add vertex """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def get_edges(self):
        """ get edges """
        edges = []
        for from_vertex in self.graph:
            for to_vertex in self.graph[from_vertex]:
                edges.append((from_vertex, to_vertex))
        return edges

    def get_vertices(self):
        """ get vertices """
        return list(self.graph.keys())
    
    def bfs(self, start_vertex):
        """ BFS """
        if start_vertex not in self.graph:
            return []
        visited = set()
        queue = deque()
        result = []
        queue.append(start_vertex)
        visited.add(start_vertex)
        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)
            for neighbor in self.graph.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def print_graph(self):
        """ print graph """
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


class GraphAdjacencyMatrix:
    """GraphAdjacencyMatrix"""
    def __init__(self):
        self.vertices = [] 
        self.vertex_index = {}
        self.matrix = []

    def add_vertex(self, vertex):
        """add vertex"""
        if vertex not in self.vertex_index:
            self.vertex_index[vertex] = len(self.vertices)
            self.vertices.append(vertex)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.vertices))

    def add_edge(self, u, v, directed=True):
        """add edge"""
        if u not in self.vertex_index:
            self.add_vertex(u)
        if v not in self.vertex_index:
            self.add_vertex(v)
        
        u_idx = self.vertex_index[u]
        v_idx = self.vertex_index[v]
        
        self.matrix[u_idx][v_idx] = 1
        if not directed:
            self.matrix[v_idx][u_idx] = 1

    def from_edge_list(self, edges, directed=True):
        """from edge list"""
        for u, v in edges:
            self.add_edge(u, v, directed)

    def print_matrix(self):
        """print matrix"""
        print("   " + " ".join(f"{v:2}" for v in self.vertices))
        for i, row in enumerate(self.matrix):
            print(f"{self.vertices[i]:2} [" + " ".join(map(str, row)) + "]")

    def get_adjacency_matrix(self):
        """get adjacency matrix"""
        return self.matrix

    def get_vertices(self):
        """get vertices"""
        return self.vertices.copy()

    def get_edges(self, directed=True):
        """get edges"""
        edges = []
        n = len(self.vertices)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    edges.append((self.vertices[i], self.vertices[j]))
                    if not directed and i > j and self.matrix[j][i] == 1:
                        edges.remove((self.vertices[j], self.vertices[i]))
        return edges

dg = DirectedGraph()
dg.add_vertex("A", "B")
dg.add_vertex("A", "C")
dg.add_vertex("B", "C")
dg.add_vertex("C", "A")

print("Список смежности:")
dg.print_graph()

print("\nВсе вершины:", dg.get_vertices())
print("Все рёбра:", dg.get_edges())

print("\nBFS, начиная с 'A':", dg.bfs('A'))
print("BFS, начиная с 'B':", dg.bfs('B'))


graph = GraphAdjacencyMatrix()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')

print("Матрица смежности:")
graph.print_matrix()
