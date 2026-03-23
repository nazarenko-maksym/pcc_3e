sandwich_orders = ['cuban', 'elvis', 'panuozzo', 'sirloin', 'pastrami']
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')

print(f"Our deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"{current_sandwich.title()} has been made!")
    finished_sandwiches.append(current_sandwich)

print("Made sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
