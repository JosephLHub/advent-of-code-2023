import sys
engine_schematic = sys.stdin.read().split("\n")
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
gear_info = {}
for x in range(len(engine_schematic)):
    current_num = ""
    num_complete = True
    neighbours = []
    for y in range(len(engine_schematic[x])):
        if engine_schematic[x][y] in digits:
            num_complete = False #Start recording new number
            current_num = current_num + engine_schematic[x][y] #Add digit to currently recorded number
            neighbours += [(x_, y_) for x_ in range(x-1, x+2) for y_ in range(y-1, y+2)
            if (0 <= x_ < len(engine_schematic) and 0 <= y_ < len(engine_schematic) and engine_schematic[x_][y_] == "*" and (x_, y_) not in neighbours)] #Get surrounding asterisks
        else:
            for asterisk in neighbours:
                print(len(neighbours))
                if current_num in list(gear_info.keys()):
                    gear_info.update({current_num : list(gear_info.get(current_num)) + [asterisk]})
                else:
                    gear_info.update({current_num : [asterisk]})
            num_complete = True #Stop recording current number
            current_num = "" #Reset
            neighbours = []
    for asterisk in neighbours:
        print(len(neighbours))
        if current_num in list(gear_info.keys()):
            gear_info.update({current_num : list(gear_info.get(current_num)) + [asterisk]})
        else:
            gear_info.update({current_num : [asterisk]})
        num_complete = True #Stop recording current number
        current_num = "" #Reset
        neighbours = []
coordinates = []
for x in list(gear_info.values()):
    for y in x:
        coordinates.append(y) #Flatten list of lists into list of all coordinate occurrences
print(coordinates)
for coord in set(coordinates):
    if coordinates.count(coord) == 2: #If asterisk is a gear
        gear_nums = []
        for num, pos in gear_info.items():
            if coord in pos:
                gear_nums.append(int(num))
                pos.remove(coord)
                if len(pos) > 0 and coord in pos:
                    gear_nums.append(int(num))
        print(gear_nums)
        sum += gear_nums[0] * gear_nums[1]
print(sum)
