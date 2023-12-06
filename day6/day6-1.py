import sys
race_info = sys.stdin.read().split("\n")
times = race_info[0][(race_info[0].index(":") + 2) :].split()
records = race_info[1][(race_info[1].index(":") + 2) :].split()
range_mult = 1
for x in range(len(times)):
    ways_to_beat = 0
    for y in range(int(times[x])):
        dist = y * (int(times[x]) - y)
        if dist > int(records[x]):
            ways_to_beat += 1
    range_mult *= ways_to_beat
print(range_mult)
