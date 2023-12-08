import sys
import math
data = sys.stdin.read().split("\n")
network = {}
for node in data[2:]:
    network.update({node[0:3] : (node[7:10], node[12:15])})
current_nodes = [key for key in network.keys() if key[2] == "A"]
print(current_nodes)
path_lengths = []
for x in range(len(current_nodes)):
    steps = 0
    while current_nodes[x][2] != "Z":
        if (data[0][steps % len(data[0])] == "L"):
            current_nodes[x] = network.get(current_nodes[x])[0]
        else:
            current_nodes[x] = network.get(current_nodes[x])[1]
        steps += 1
    path_lengths.append(steps)
lcm = 1
for path in path_lengths:
    lcm = (lcm * path) // math.gcd(lcm, path)
print(lcm)