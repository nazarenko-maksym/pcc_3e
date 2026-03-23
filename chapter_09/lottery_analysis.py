from random import choice
import statistics

LOTTERIES = 10000
LOT = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

rolls_stats = []

for times in range(LOTTERIES):
    my_ticket = []
    for roll in range(4):
        my_ticket.append(choice(LOT))
    winner = []
    rolls = 0
    while my_ticket != winner:
        winner = []
        rolls += 1
        for chance in range(4):
            winner.append(choice(LOT))
    rolls_stats.append(rolls)

print(f"After \"{LOTTERIES}\" lotteries, we have:")
print(f'  min   : {format(min(rolls_stats))}')
print(f'  max   : {format(max(rolls_stats))}')
print(f'  mean  : {format(statistics.mean(rolls_stats))}')
