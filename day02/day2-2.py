import sys
game_records = sys.stdin.read().split("\n")
sum = 0
def get_min(colour):
    min_amount = 0
    while colour in game_records[x]:
        pos = game_records[x].find(colour) - 2
        if game_records[x][pos-1] != " ":
            amount = int(game_records[x][pos-1:pos+1])
        else:
            amount = int(game_records[x][pos])
        min_amount = max(min_amount, amount)
        game_records[x] = game_records[x].replace(colour, "", 1)
    return min_amount
for x in range(len(game_records)):
    sum += (get_min("red") * get_min("green") * get_min("blue"))
print(sum)