import sys
almanac = sys.stdin.read().split("\n")
map_titles = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]
seed_ranges = almanac[0][(almanac[0].index(":") + 2) :].split() #Obtain list of seed numbers at top of almanac
seed_nums = []
for x in range(len(seed_ranges)):
    if x % 2 == 0:
        seed_nums += list(set(range(int(seed_ranges[x]), int(seed_ranges[x]) + int(seed_ranges[x+1]))))
        print("Done")
print(len(seed_nums))
for title in map_titles:
    current_map = almanac[almanac.index(title) + 1 : almanac.index("", almanac.index(title))] #Extract each map from almanac based on line preceeding it
    for x in range(len(seed_nums)):
        for section in current_map:
            ranges = section.split()
            if seed_nums[x] >= int(ranges[1]) and seed_nums[x] < (int(ranges[1]) + int(ranges[2])): #Check if number is within each range
                seed_nums[x] = (int(ranges[0]) + (seed_nums[x] - int(ranges[1]))) #Start at destination range & add difference between previous number & start of source range
                break #Ensure number cannot be modified further in this iteration
    seed_nums = list(set(seed_nums))
    print(len(seed_nums))
print(min(seed_nums))

# answer = 79874951