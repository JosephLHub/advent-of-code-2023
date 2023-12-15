import sys
almanac = sys.stdin.read().split("\n")
map_titles = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]
seed_ranges = almanac[0][(almanac[0].index(":") + 2) :].split() #Obtain list of seed numbers at top of almanac
seed_nums = set()
for x in range(len(seed_ranges)):
    if x % 2 == 0:
        seed_nums.update(range(int(seed_ranges[x]), int(seed_ranges[x]) + int(seed_ranges[x+1])))
        print("Done")
for title in map_titles:
    current_map = almanac[almanac.index(title) + 1 : almanac.index("", almanac.index(title))] #Extract each map from almanac based on line preceeding it
    new_nums = set()
    for section in current_map:
        ranges = [int(i) for i in section.split()]
        min_ = ranges[1]
        max_ = ranges[1] + ranges[2]
        dest = ranges[0]
        if len(seed_nums) > 0 and min(seed_nums) < max_:
            if min(seed_nums) >= min_ and max(seed_nums) < max_: #If entire set of nums is in section
                remove_nums = set([num for num in seed_nums])
                new_nums.update([(dest + num - min_) for num in seed_nums])
            elif min(seed_nums) >= min_: #If all nums are at least over the lower bound
                remove_nums = set([num for num in seed_nums if num < max_])
                new_nums.update([(dest + num - min_) for num in seed_nums if num < max_])
            elif max(seed_nums) < max_: #If all nums are at most under the lower bound
                remove_nums = set([num for num in seed_nums if min_ <= num])
                new_nums.update([(dest + num - min_) for num in seed_nums if min_ <= num])
            else: #If range of nums exceeds range of section
                remove_nums = set([num for num in seed_nums if min_ <= num < max_])
                new_nums.update([(dest + num - min_) for num in seed_nums if min_ <= num < max_])
        print("section check")
        seed_nums -= remove_nums
        print(len(seed_nums))
    seed_nums.update(new_nums)
    print(len(seed_nums))
print(min(seed_nums))