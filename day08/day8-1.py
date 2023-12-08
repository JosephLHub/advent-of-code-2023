import sys
data = sys.stdin.read().split("\n")
network = {}
for node in data[2:]:
    network.update({node[0:3] : (node[7:10], node[12:15])})
current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    if (data[0][steps % len(data[0])] == "L"):
        current_node = network.get(current_node)[0]
    else:
        current_node = network.get(current_node)[1]
    steps += 1
print(steps)