import sys
data = sys.stdin.read().split("\n")
def main(diffs):
    if not all(int(x) == 0 for x in diffs):
        next_ = int(diffs[-1]) + main([int(z) - int(y) for y, z in zip(diffs[:-1], diffs[1:])])
    else:
        next_ = 0
    return next_
sum = 0
for history in data:
    sum += main(history.split())
print(sum)