guests = ['charlie munger', 'steve jobs', 'alan turing']
guests.insert(0, 'donald knuth')
guests.insert(3, 'ada lovelace')
guests.append('geoffrey hinton')

print(f"Hello, {guests[0].title()}! Welcome to the dinner!")
print(f"Hello, {guests[1].title()}! Welcome to the dinner!")
print(f"Hello, {guests[2].title()}! Welcome to the dinner!")
print(f"Hello, {guests[3].title()}! Welcome to the dinner!")
print(f"Hello, {guests[4].title()}! Welcome to the dinner!")
print(f"Hello, {guests[5].title()}! Welcome to the dinner!")

print("We can invite only two people for the dinner.")

print(f"{guests.pop().title()}, we can't invite you to the dinner.")
print(f"{guests.pop().title()}, we can't invite you to the dinner.")
print(f"{guests.pop().title()}, we can't invite you to the dinner.")
print(f"{guests.pop().title()}, we can't invite you to the dinner.")

del guests[0]
del guests[0]

print(guests)
