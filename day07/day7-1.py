import sys
hand_info = sys.stdin.read().split("\n")
info_dict = {}
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
index = ["m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]

for info in hand_info:
    info_dict.update({info[:info.index(" ")] : int(info[info.index(" ") + 1 :])}) #Add card string and bid number to dictionary
rank_dict = {}
for hand in info_dict.keys():
    counts = []
    for card in cards:
        counts.append(hand.count(card))
    if 5 in counts:
        rank_dict.update({hand : 6})
    elif 4 in counts:
        rank_dict.update({hand : 5})
    elif 3 in counts and 2 in counts:
        rank_dict.update({hand : 4})
    elif 3 in counts:
        rank_dict.update({hand : 3})
    elif counts.count(2) == 2:
        rank_dict.update({hand : 2})
    elif counts.count(2) == 1:
        rank_dict.update({hand : 1})
    else:
        rank_dict.update({hand : 0})
rank_dict = dict(sorted(rank_dict.items(), key = lambda x:x[1])) #Sort dictionary by value
sorted_dict = {}
for hand in set(rank_dict.values()): #For each type of hand after ranking
    inter_rank_dict = {}
    for item in rank_dict.items():
        if item[1] == hand:
            convert = str(item[0])
            for x in range(len(cards)):
                convert = convert.replace(cards[x], index[x]) #Converts hand into alphabet to enable ordering
            inter_rank_dict.update({convert : info_dict.get(item[0])})
    inter_rank_dict = dict(sorted(inter_rank_dict.items(), key = lambda x:x[0])) #Sort dictionary by key
    sorted_dict.update(inter_rank_dict)
sum = 0
for x in range(len(sorted_dict.keys())):
    sum += ((x+1) * list(sorted_dict.values())[x])
print(sum)