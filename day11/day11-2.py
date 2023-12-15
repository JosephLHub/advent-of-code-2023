import sys
universe = sys.stdin.read().split("\n")
expanded_universe = []
cols = []
rows = []
galaxies = {}

for x in range(len(universe)):
    if all(x_ == "." for x_ in universe[x]): #If row only contains empty space
        rows.append(x) #Add to list of empty row positions

for y in range(len(universe[0])):
    if all(universe[x_][y_] == "." for x_ in range(len(universe)) for y_ in range(y, y+1)): #If column only contains empty space
        cols.append(y) #Add to list of empty column positions

galaxy_count = 0
for x in range(len(universe)):
    for y in range(len(universe[x])):
        if universe[x][y] == "#":
            gaps = 0
            for empty in rows:
                if empty < x:
                    gaps += 1
            new_x = x + (999999 * gaps)
            print(str(x) + " | " + str(new_x))
            gaps = 0
            for empty in cols:
                if empty < y:
                    gaps += 1
            new_y = y + (999999 * gaps)
            galaxies[galaxy_count] = (new_x, new_y)
            galaxy_count += 1
sum = 0
paired = []
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy2 not in paired:
            sum += (abs(galaxies[galaxy1][0] - galaxies[galaxy2][0]) + abs(galaxies[galaxy1][1] - galaxies[galaxy2][1]))
    paired.append(galaxy1)

print(sum)