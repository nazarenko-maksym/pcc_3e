toppings = []

flag = True
prompt = "What topping would you like to add? "
prompt += "\nWrite 'quite' to exit.\n"

while True:
    topping = input(prompt)
    if topping == 'quite':
        break
    print(f"We will add the \"{topping}\" tp your pizza.")
