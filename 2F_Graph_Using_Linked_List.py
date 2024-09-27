# Node class for adjacency list (linked list node)
class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None

# Graph class
class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = [None] * self.V  # Create an array of adjacency lists for each vertex

    # Add edge to the graph (undirected)
    def add_edge(self, src, dest):
        # Add an edge from src to dest
        new_node = Node(dest)
        new_node.next = self.graph[src]
        self.graph[src] = new_node

        # Since it's undirected, add an edge from dest to src
        new_node = Node(src)
        new_node.next = self.graph[dest]
        self.graph[dest] = new_node

    # Print the graph (adjacency list)
    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}:", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print()

    # Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = [False] * self.V
        queue = [start_vertex]
        visited[start_vertex] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            temp = self.graph[vertex]
            while temp:
                if not visited[temp.vertex]:
                    queue.append(temp.vertex)
                    visited[temp.vertex] = True
                temp = temp.next
        print()

    # Depth-First Search (DFS)
    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        temp = self.graph[vertex]
        while temp:
            if not visited[temp.vertex]:
                self.dfs_util(temp.vertex, visited)
            temp = temp.next

    def dfs(self, start_vertex):
        visited = [False] * self.V
        self.dfs_util(start_vertex, visited)
        print()


# Example Usage
if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    print("Graph adjacency list:")
    graph.print_graph()

    print("\nBreadth-First Search (starting from vertex 0):")
    graph.bfs(0)

    print("\nDepth-First Search (starting from vertex 0):")
    graph.dfs(0)


# ******************************************************************

### Explanation:
    # 1. Node cla : Represents a node in the adjacency list.
    # 2. Graph cla : Manages the graph:
    #     add_ed : Adds edges to the graph, creating an adjacency list for each vertex.
    #     print_gra : Displays the adjacency list for each vertex.
    #     b : Performs Breadth-First Search from a starting vertex.
    #     d : Performs Depth-First Search from a starting vertex.    


### Output:
    # Graph adjacency list:
    # Adjacency list of vertex 0: -> 4 -> 1
    # Adjacency list of vertex 1: -> 4 -> 3 -> 2 -> 0
    # Adjacency list of vertex 2: -> 3 -> 1
    # Adjacency list of vertex 3: -> 4 -> 2 -> 1
    # Adjacency list of vertex 4: -> 3 -> 1 -> 0

    # Breadth-First Search (starting from vertex 0):
    # 0 1 4 2 3

    # Depth-First Search (starting from vertex 0):
    # 0 1 2 3 4



### Key Points:
# - This code creates a simple graph with *5 vertices*.
# - It adds edges between vertices and displays the *adjacency list*.
# - It implements *BFS* and *DFS* to traverse the graph starting from vertex 0.