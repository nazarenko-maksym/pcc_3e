current_users = ['max', 'artur', 'vlad', 'daria', 'willow']
new_users = ['miko', 'marie', 'katrya', 'daria', 'willow']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user}, you need to enter a new username.")
    else:
        print(f"The username {new_user} is available.")
