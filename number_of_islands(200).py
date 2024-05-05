grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(i,j)
        print(grid[i][j])


def create_graph(grid):
  # Initialize an empty graph
  graph = {}
  
  # Get the number of rows and columns in the grid
  rows = len(grid)
  cols = len(grid[0])
  
  # Iterate through each cell in the grid
  for i in range(rows):
    for j in range(cols):
      # Check if the cell contains '1'
      if grid[i][j] == "1":
        # Calculate the node index based on the row and column
        node = i * cols + j
        # Add the node to the graph with an empty list of adjacent nodes
        graph[node] = []
        
        # Check if the cell above contains '1' and connect it to the current node
        if i > 0 and grid[i-1][j] == "1":
          graph[node].append((i-1) * cols + j)
        
        # Check if the cell below contains '1' and connect it to the current node
        if i < rows-1 and grid[i+1][j] == "1":
          graph[node].append((i+1) * cols + j)
        
        # Check if the cell to the left contains '1' and connect it to the current node
        if j > 0 and grid[i][j-1] == "1":
          graph[node].append(i * cols + (j-1))
        
        # Check if the cell to the right contains '1' and connect it to the current node
        if j < cols-1 and grid[i][j+1] == "1":
          graph[node].append(i * cols + (j+1))
  
    return graph
  print(graph)

create_graph(grid)