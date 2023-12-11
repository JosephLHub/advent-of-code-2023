import sys
field = sys.stdin.read().split("\n")
paths = []
directions = []
cardinals = ["N", "E", "S", "W"]
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
def find_farthest(field, coords, directions):
    path_length = 1
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
        path_length += 1
    return path_length

print(find_farthest(field, paths, directions))