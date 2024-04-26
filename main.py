import json

class User:
    def __init__(self, username, name, age, email, password):
        self.username = username
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def view_profile(self):
        print("Name:", self.name) 
        print("Age:", self.age)
        print("Email:", self.email)

    def update_profile(self, new_name, new_age, new_email):
        self.name = new_name
        self.age = new_age
        self.email = new_email
        print("Profile updated successfully!")

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "Not Done"
        print("Tasks Added...")

    def view_task(self):
        print("\nTasks")
        for key in self.tasks:
            print(f"{key}: {self.tasks[key]}")

    def mark_as_done(self, task):
        self.tasks[task] = "Done"

    def save_to_file(self, username):
        with open(f"{username}_todolist.txt", "w") as f:
            json.dump(self.tasks, f)

    def load_from_file(self, username):
        try:
            with open(f"{username}_todolist.txt", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = {}

class Menu:
    def __init__(self):
        self.user_database = {
            "sumukh29": User("sumukh29", "Sumukh", 18, "sumukh@gmail.com", "12345"),
            "amit10": User("amit10", "Amit", 20, "amit@gmail.com", "abcdef")
        }

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.user_database and self.user_database[username].password == password:
            print("Login successful!")
            return self.user_database[username]
        else:
            print("Invalid username or password")
            return None

    def main_menu(self):
        while True:
            print("\nMenu:")
            print("1. Login")
            print("2. View Profile")
            print("3. Update Profile")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                user = self.login()
                if user:
                    todo_list = ToDoList()
                    todo_list.load_from_file(user.username)
                    self.to_do_menu(todo_list, user)
            elif choice == "2":
                print("\nView Profile:")
                user = self.login()
                if user:
                    user.view_profile()
            elif choice == "3":
                print("\nUpdate Profile:")
                user = self.login()
                if user:
                    new_name = input("Enter new name: ")
                    new_age = input("Enter new age: ")
                    new_email = input("Enter new email: ")
                    user.update_profile(new_name, new_age, new_email)
            elif choice == "4":
                print("Exiting program...")
                break
            else:
                print("Invalid choice, please try again.")

    def to_do_menu(self, todo_list, user):
        while True:
            print("\nTO-DO List:")
            print("1. Add Task")
            print("2. View Task")
            print("3. Mark as Done")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                num = int(input("Enter number of tasks : "))
                for i in range(num):
                    task = input("Enter Task : ")
                    todo_list.add_task(task)
                print("Tasks Added...")
                todo_list.save_to_file(user.username)
            elif choice == "2":
                todo_list.view_task()
            elif choice == "3":
                taskdone = input("Enter task to mark done : ")
                todo_list.mark_as_done(taskdone)
                todo_list.save_to_file(user.username)
            elif choice == '4':
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")

menu = Menu()
menu.main_menu()