import sys
engine_schematic = sys.stdin.read().split("\n")
symbols = ['*', '@', '=', '%', '+', '$', '&', '/', '-', '#']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
current_num = ""
part_number = False
for x in range(len(engine_schematic)):
    if part_number:
        sum += int(current_num)
        part_number = False
        current_num = ""
    for char in range(len(engine_schematic[x])):
        if engine_schematic[x][char] in digits:
            current_num = current_num + engine_schematic[x][char] #Start recording part number
            neighbours = [engine_schematic[x_][char_] for x_ in range(x-1, x+2) for char_ in range(char-1, char+2)
            if (0 <= x_ < len(engine_schematic) and 0 <= char_ < len(engine_schematic))] #Makes 3x3 window surrounding current position
            if (len(set(neighbours).intersection(set(symbols))) > 0): #If any surrounding position has a symbol
                part_number = True
        else:
            print(engine_schematic[x][char])
            if part_number:
                sum += int(current_num)
                part_number = False
            current_num = ""
print(sum)