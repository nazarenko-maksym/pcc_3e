num_of_people = input("How many people are in your dinner group? ")
num_of_people = int(num_of_people)
if num_of_people > 8:
    print(f"You will have to wait for a table.")
else:
    print(f"Your table is ready.")
