import sys
mirrors = sys.stdin.read().split("\n\n")
sum = 0

def valid_reflection(grid, index):
    i = index
    j = index + 1
    while i >= 0 and j < len(grid):
        if grid[i] != grid[j]:
            return False
        i -= 1
        j += 1
    return True

for mirror in mirrors:
    grid = [list(line) for line in mirror.split("\n")]
    for i in range(len(grid) - 1):
        if valid_reflection(grid, i):
            sum += 100 * (i+1)
    grid_t = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    for i in range(len(grid_t) - 1):
        if valid_reflection(grid_t, i):
            sum += i+1
print(sum)