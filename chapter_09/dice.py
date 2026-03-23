from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

die = Die(6)
for roll in range(10):
    print(f"Roll {die.sides}-sided die: {die.roll_die()}")

die_10 = Die(10)
for roll in range(10):
    print(f"Roll {die_10.sides}-sided die: {die_10.roll_die()}")

die_20 = Die(20)
for roll in range(10):
    print(f"Roll {die_20.sides}-sided die: {die_20.roll_die()}")
