# DFS function
def dfs(adjList, start, visited=None):
    if visited is None:
        visited = [False] * len(adjList)

    # Mark the current node as visited
    visited[start] = True
    print(start, end=" ")

    # Recur for all the vertices adjacent to this vertex
    for neighbor in adjList[start]:
        if not visited[neighbor]:
            dfs(adjList, neighbor, visited)

# Function to add an edge to the graph
def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    # Number of vertices in the graph
    vertices = 5
    # Initialize adjacency list
    adjList = [[] for _ in range(vertices)]
    # Add edges to the graph
    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 2)
    addEdge(adjList, 2, 0)
    addEdge(adjList, 2, 3)
    addEdge(adjList, 3, 3)
    # Perform DFS
    print("Depth First Traversal (starting from vertex 2):")
    dfs(adjList, 2)
main()