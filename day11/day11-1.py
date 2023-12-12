import sys
universe = sys.stdin.read().split("\n")
empty_rows = []
def expand(rows, cols):
    for x in range(rows):
        universe.insert(rows[x], universe[rows[x]]) #Duplicate row
    for y in range(cols):
        universe

for row in range(len(universe)):
    if all(x == "." for x in universe[row]): #If row only contains empty space
        empty_rows.append(row)
