import sys
mirrors = sys.stdin.read().split("\n\n")
sum_ = 0

def valid_reflection(grid, index):
    has_smudged = False
    i = index
    j = index + 1
    while i >= 0 and j < len(grid):
        if grid[i] != grid[j]:
            if has_smudged:
                return False
            common = sum(a == b for a, b in zip(grid[i], grid[j]))
            if common != len(grid[i]) - 1: #If smudging doesn't create a reflection
                return False
            has_smudged = True
        i -= 1
        j += 1
    return has_smudged

for mirror in mirrors:
    grid = [list(line) for line in mirror.split("\n")]
    for i in range(len(grid) - 1):
        if valid_reflection(grid, i):
            sum_ += (100 * (i+1))

    grid_t = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

    for i in range(len(grid_t) - 1):
        if valid_reflection(grid_t, i):
            sum_ += (i+1)
print(sum_)