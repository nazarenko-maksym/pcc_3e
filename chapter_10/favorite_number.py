from pathlib import Path
import json


def get_stored_f_number(path):
    """Get favorite number if available"""
    if path.exists():
        content = path.read_text()
        f_number = json.loads(content)
        return f_number
    else:
        return None

def get_new_f_number(path):
    """Prompt for a new favorite number"""
    f_number = input("What is your favorite number? ")
    content = json.dumps(f_number)
    path.write_text(content)
    return f_number

def show_f_number():
    """Reads favorite number"""
    path = Path('fav_number.json')
    f_number = get_stored_f_number(path)
    if f_number:
        print(f"Your favorite number is \"{f_number}\"")
    else:
        f_number = get_new_f_number(path)
        print(f"Next time we will remember your favorite number {f_number}")


show_f_number()
