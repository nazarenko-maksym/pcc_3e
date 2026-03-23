guests = ['charlie munger', 'steve jobs', 'alan turing']

print(f"Hello, {guests[0].title()}! Welcome to the dinner!")
print(f"Hello, {guests[1].title()}! Welcome to the dinner!")
print(f"Hello, {guests[2].title()}! Welcome to the dinner!")

print(f"{guests[1].title()} can't attend the dinner.")

guests[1] = 'donald knuth'

print(f"Hello, {guests[0].title()}! Welcome to the dinner!")
print(f"Hello, {guests[1].title()}! Welcome to the dinner!")
print(f"Hello, {guests[2].title()}! Welcome to the dinner!")
