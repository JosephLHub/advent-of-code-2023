import sys
game_records = sys.stdin.read().split("\n")
sum = 0
def colour_check(colour, count):
    while colour in game_records[x]:
        pos = game_records[x].find(colour) - 2
        if game_records[x][pos-1] != " ":
            if int(game_records[x][pos-1:pos+1]) > count:
                return False
        game_records[x] = game_records[x].replace(colour, "", 1)
    return True

for x in range(len(game_records)):
    game_records[x] = game_records[x].replace("Game", "")
    if colour_check("red", 12) and colour_check("green", 13) and colour_check("blue", 14):
        sum += int(game_records[x][0:(game_records[x].index(":"))])
print(sum)
