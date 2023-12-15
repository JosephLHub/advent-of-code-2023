import sys
universe = sys.stdin.read().split("\n")
expanded_universe = []
cols = []
galaxies = {}

for row in universe:
    if all(x == "." for x in row): #If row only contains empty space
        expanded_universe.append(row)
    expanded_universe.append(row)

for y in range(len(expanded_universe[0])):
    if all(expanded_universe[x_][y_] == "." for x_ in range(len(expanded_universe)) for y_ in range(y, y+1)): #If column only contains empty space
        cols.append(y + len(cols))
for x in range(len(expanded_universe)):
    row = list(expanded_universe[x])
    for pos in cols:
        row.insert(pos, ".") #Add duplicated columns
    expanded_universe[x] = "".join(row)

galaxy_count = 0
for x in range(len(expanded_universe)):
    for y in range(len(expanded_universe[x])):
        if expanded_universe[x][y] == "#":
            galaxies[galaxy_count] = (x, y)
            galaxy_count += 1
sum = 0
paired = []
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy2 not in paired:
            sum += (abs(galaxies[galaxy1][0] - galaxies[galaxy2][0]) + abs(galaxies[galaxy1][1] - galaxies[galaxy2][1]))
    paired.append(galaxy1)

print(sum)