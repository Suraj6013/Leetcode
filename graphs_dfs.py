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

    while True:
        print("\n1. Add edge")
        print("2. Perform DFS")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = int(input("Enter the source vertex: "))
            v = int(input("Enter the destination vertex: "))
            addEdge(adjList, u, v)
        elif choice == 2:
            start = int(input("Enter the starting vertex for DFS: "))
            print("Depth First Traversal (starting from vertex {}):".format(start))
            dfs(adjList, start)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
main()