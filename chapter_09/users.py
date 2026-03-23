class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} living in {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

user_1 = User('max', 'min', '100', 'kyiv')
user_2 = User('willow', 'miko', '2', 'boston')
