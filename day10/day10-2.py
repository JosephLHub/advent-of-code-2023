import sys
field = sys.stdin.read().split("\n")
paths = []
directions = []
cardinals = ["N", "E", "S", "W"]
def get_path(field, coords, directions):
    tiles = []
    while not coords[0] == coords[1]:
        for x in range(2):
            match field[coords[x][0]][coords[x][1]]:
                case "|":
                    coords[x] = (coords[x][0] - 1, coords[x][1]) if directions[x] == "N" else (coords[x][0] + 1, coords[x][1])
                case "-":
                    coords[x] = (coords[x][0], coords[x][1] - 1) if directions[x] == "W" else (coords[x][0], coords[x][1] + 1)
                case "F":
                    coords[x] = (coords[x][0], coords[x][1] + 1) if directions[x] == "N" else (coords[x][0] + 1, coords[x][1])
                    directions[x] = "E" if directions[x] == "N" else "S"
                case "7":
                    coords[x] = (coords[x][0], coords[x][1] - 1) if directions[x] == "N" else (coords[x][0] + 1, coords[x][1])
                    directions[x] = "W" if directions[x] == "N" else "S"
                case "L":
                    coords[x] = (coords[x][0], coords[x][1] + 1) if directions[x] == "S" else (coords[x][0] - 1, coords[x][1])
                    directions[x] = "E" if directions[x] == "S" else "N"
                case "J":
                    coords[x] = (coords[x][0], coords[x][1] - 1) if directions[x] == "S" else (coords[x][0] - 1, coords[x][1])
                    directions[x] = "W" if directions[x] == "S" else "N"
            tiles.append(coords[x])
    return set(tiles)

for x in range(len(field)):
    for y in range(len(field[x])):
        if field[x][y] == "S":
            if field[x-1][y] == "|" or field[x-1][y] == "F" or field[x-1][y] == "7":
                paths.append((x-1, y))
                directions.append(cardinals[0])
            if field[x][y+1] == "-" or field[x][y-1] == "J" or field[x][y-1] == "7":
                paths.append((x, y+1))
                directions.append(cardinals[1])
            if field[x+1][y] == "|" or field[x+1][y] == "L" or field[x+1][y] == "J":
                paths.append((x+1, y))
                directions.append(cardinals[2])
            if field[x][y-1] == "-" or field[x][y-1] == "F" or field[x][y-1] == "L":
                paths.append((x, y-1))
                directions.append(cardinals[3])
            field[x][y].replace("S", "F")
tiles = list(get_path(field, paths, directions))
print(tiles)

def is_in(tiles, field, x, y):
    line = ""
    for north in range(x):
        if (north, y) in tiles and field[north][y] != "|" and field[x][north] != ".":
            line = line + field[north][y]
    if len(line) == 0:
        return False
    line = line.replace("FJ", "F").replace("FL", "F").replace("7L", "7").replace("7J", "7")
    if len(line) % 2 == 1:
        return True
    line = ""
    for south in range(x+1, len(field)):
        if (south, y) in tiles and field[south][y] != "|" and field[x][south] != ".":
            line = line + field[south][y]
    if len(line) == 0:
        return False
    line = line.replace("FJ", "F").replace("FL", "F").replace("7L", "7").replace("7J", "7")
    if len(line) % 2 == 1:
        return True
    line = ""
    for west in range(y):
        if (x, west) in tiles and field[x][west] != "-" and field[x][west] != ".":
            line = line + field[x][west]
    if len(line) == 0:
        return False
    line = line.replace("FJ", "F").replace("LJ", "L").replace("F7", "F").replace("L7", "L")
    if len(line) % 2 == 1:
        return True
    line = ""
    for east in range(y+1, len(field[x])):
        if (x, east) in tiles and field[x][east] != "-" and field[x][east] != ".":
            line = line + field[x][east]
    if len(line) == 0:
        return False
    line = line.replace("FJ", "F").replace("LJ", "L").replace("F7", "F").replace("L7", "L")
    if len(line) % 2 == 1:
        return True
    return False
    
sum = 0
for x in range(len(field)):
    for y in range(len(field[x])):
        if (x, y) not in tiles and 0 < x < (len(field) - 1) and 0 < y < (len(field[x]) - 1):
            if is_in(tiles, field, x, y):
                print(x, y)
                sum += 1
print(sum)

#Count how many tiles crossed over until reaching edge in each direction
#Ignore | when searching vertically, ignore - when searching horizontally
#Count FJ, LJ, L7, F7 combos as 1 if they align w/ direction being searched