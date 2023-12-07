import sys
almanac = sys.stdin.read().split("\n")
map_titles = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]
seed_nums = almanac[0][(almanac[0].index(":") + 2) :].split() #Obtain list of seed numbers at top of almanac
for title in map_titles:
    current_map = almanac[almanac.index(title) + 1 : almanac.index("", almanac.index(title))] #Extract each map from almanac based on line preceeding it
    for x in range(len(seed_nums)):
        for section in current_map:
            if int(seed_nums[x]) >= int(section.split()[1]) and int(seed_nums[x]) < (int(section.split()[1]) + int(section.split()[2])): #Check if number is within each range
                seed_nums[x] = (int(section.split()[0]) + (int(seed_nums[x]) - int(section.split()[1]))) #Start at destination range & add difference between previous number & start of source range
                break #Ensure number cannot be modified further in this iteration
print(min(seed_nums))