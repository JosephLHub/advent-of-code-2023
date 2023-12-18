import sys
platform = sys.stdin.read().split("\n")
platform_t = [[platform[i][j] for i in range(len(platform))] for j in range(len(platform[0]))]
for x in range(len(platform_t)):
    for y in range(len(platform_t[x])):
        if platform_t[x][y] == "O":
            i = 1
            while True:
                if  y-i >= 0 and platform_t[x][y-i] == ".":
                    platform_t[x][y-i+1] = "."
                    platform_t[x][y-i] = "O"
                    i += 1
                else:
                    break
total = 0
for x in range(len(platform_t)):
    for y in range(len(platform_t[x])):
        if platform_t[x][y] == "O":
            total += (len(platform_t[x]) - y)
print (total)