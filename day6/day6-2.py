import sys
race_info = sys.stdin.read().split("\n")
time = int(race_info[0][(race_info[0].index(":") + 2) :].replace(" ", ""))
record = int(race_info[1][(race_info[1].index(":") + 2) :].replace(" ", ""))
ways_to_beat = 0
for x in range(time):
    dist = x * (time - x)
    if dist > record:
        ways_to_beat += 1
print(ways_to_beat)