from functools import cache
import sys
records = sys.stdin.read().split("\n")
springs = []
nums = []
sum = 0
@cache
def valid_layouts(layout, data, last_hash):
    #Empty layout
    if len(layout) == 0:
        return len(data) == 0
    match layout[0]:
        case ".":
            if last_hash: #Check if current string is fully consumed
                if len(data) == 0 or data[0] != 0:
                    return 0
                data = data [1:]
            return valid_layouts(layout[1:], data, False)
        case "#": #Consume current string
            if len(data) == 0:
                return 0
            data = tuple(tuple([data[0] - 1]) + data[1:])
            if data[0] < 0:
                return 0
            return valid_layouts(layout[1:], data, True)
        case "?": #Split into . and # cases
            return valid_layouts("." + layout[1:], data, last_hash) + valid_layouts("#" + layout[1:], data, last_hash)
    raise Exception ("oh lord")

for record in records: #Split record up into spring data and num data
    springs, right = record.split()
    nums = tuple([int(y) for y in right.split(",")] * 5)
    new_springs = "?".join([springs] * 5)
    sum += valid_layouts(new_springs + ".", nums, False)
print(sum)