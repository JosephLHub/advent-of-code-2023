import sys
engine_schematic = sys.stdin.read().split("\n")
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
is_gear = False
for x in range(len(engine_schematic)):
    for y in range(len(engine_schematic[x])):
        if engine_schematic[x][y] == "*":
            neighbours = [engine_schematic[x_][y_] for x_ in range(x-1, x+2) for y_ in range(y-1, y+2)
            if (0 <= x_ < len(engine_schematic) and 0 <= y_ < len(engine_schematic))] #Makes 3x3 window surrounding current position
            print(neighbours[0], " ", neighbours[1], " ", neighbours[2])
            print(neighbours[3], " ", neighbours[4], " ", neighbours[5])
            print(neighbours[6], " ", neighbours[7], " ", neighbours[8])
            
                    
print(sum)

#If neighbour = number, find whole number
    #Travel forwards & backwards until non-numbers are found