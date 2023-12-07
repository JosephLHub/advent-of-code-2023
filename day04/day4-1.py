import sys, math
cards = sys.stdin.read().split("\n")
sum = 0
for nums in cards:
    winning_nums = nums[nums.index(":") + 2 : nums.index("|") - 1].split() #Extract list of winning numbers
    card_nums = nums[nums.index("|") + 2 :].split() #Extract list of card numbers
    matches = len(set(winning_nums).intersection(set(card_nums))) #Get amount of numbers in common
    if matches > 0:
        sum += math.pow(2, (matches - 1)) #Calculate points from amount of matches
print(sum)