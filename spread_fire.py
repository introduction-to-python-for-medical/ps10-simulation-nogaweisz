import copy

def spread_fire(grid):
  
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid) 

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # If the cell contains a tree
                neighbors = []
                # Check all four neighboring cells
                if i > 0:
                    neighbors.append(grid[i-1][j])  # Top neighbor
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])  # Bottom neighbor
                if j > 0:
                    neighbors.append(grid[i][j-1])  # Left neighbor
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])  # Right neighbor

                # If any neighbor is on fire, the current tree catches fire
                if 2 in neighbors: 
                    update_grid[i][j] = 2 

    return update_grid

