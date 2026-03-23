from random import choice

lot = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']

winner = []

for roll in range(4):
    winner.append(str(choice(lot)))

print(f"Any ticket matching these 4 numbers or letters wins a prize:\n-", "".join(winner))
