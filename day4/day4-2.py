import sys, math
cards = sys.stdin.read().split("\n")
sum = 0
copy_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for nums in cards:
    cards_in_play = copy_counts[0] + 1
    copy_counts.pop(0) #Remove current copy count from the queue
    copy_counts.append(0) #Return list size to normal
    winning_nums = nums[nums.index(":") + 2 : nums.index("|") - 1].split() #Extract list of winning numbers
    card_nums = nums[nums.index("|") + 2 :].split() #Extract list of card numbers
    matches = len(set(winning_nums).intersection(set(card_nums))) #Get amount of numbers in common
    print(matches)
    for x in range(matches):
        copy_counts[x] += cards_in_play
    print(copy_counts)
    sum += cards_in_play
print(sum)

#Add copy counts based on matches
#remove front of copy counts every iteration & add to cards in play