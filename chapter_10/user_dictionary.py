from pathlib import Path
import json


def greet_user():
    path = Path('user_dictionary.json')
    if path.exists():
        user_info = get_user_info(path)
    else:
        user_info = store_user_info(path)
    flag = input(f"Is \"{user_info['user_name']}\" a correct name? ")
    if flag not in ['yes', 'y', 'Yes', 'YES', 'Y']:
        user_info = update_user_name(path)
    print(f"Welcome back, {user_info['user_name']}!")
    for k, v in user_info.items():
        print(f"{k} is {v}")

def store_user_info(path):
    user_name = input("What is your name? ")
    while True:
        try:
            user_age = input("What is your age? ")
            user_age = int(user_age)
        except:
            print("User age must be a digit.")
            user_age = ""
        if user_age:
            break
    user_location = input("What is your location? ")
    user_info = {
        'user_name': user_name,
        'user_age': user_age,
        'user_location': user_location,
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def get_user_info(path):
    contents = path.read_text()
    user_info = json.loads(contents)
    return user_info

def update_user_name(path):
    contents = path.read_text()
    user_info = json.loads(contents)
    user_name = input("What is your name? ")
    user_info['user_name'] = user_name
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

greet_user()
