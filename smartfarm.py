import sqlite3
import hashlib
import os

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.progress = {"Educational Modules": 0, "Q&A Sessions": 0, "Job Applications": 0}

class SmartFarmingPlatform:
    def __init__(self):
        self.conn = sqlite3.connect("smart_farming.db")
        self.create_tables()
        self.users = {}
        self.notifications = []

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self.conn.commit()

    def authenticate_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        return cursor.fetchone()

    def introduction(self):
        print("Welcome to the Smart Farming Platform!")
        print("Our mission is to empower farmers through education, collaboration, and employment opportunities.")
        print("Let's embark on this journey together!\n")

    def start_prompt(self):
        while True:
            choice = input("Are you a registered user? (yes/no): ").lower()

            if choice == "yes":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user_data = self.authenticate_user(username, password)
                if user_data:
                    print(f"\nWelcome back, {username}!")
                    break
                else:
                    print("Invalid credentials. Please try again.\n")
            elif choice == "no":
                username = input("Enter a username: ")
                password = input("Create a password: ")
                self.register_user(username, password)
                print("Registration successful! You can now log in.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")

    def display_dashboard(self):
        print("\n=== Smart Farming Dashboard ===")
        print("1. Educational Modules")
        print("2. Live Q&A")
        print("3. Job Portal")
        print("4. Check Progress")
        print("5. Notifications")
        print("6. Exit")

    # ... (rest of the methods remain unchanged)

    def main(self):
        self.introduction()
        self.start_prompt()
        while True:
            username = input("Enter your username: ")
            if username not in self.users:
                self.users[username] = User(username, username)  # You can customize the user creation logic
            user = self.users[username]
            self.display_dashboard()
            choice = input("\nEnter the number of your choice:")
            if choice == "1":
                self.educational_module(user)
            elif choice == "2":
                self.qna_interaction(user)
            elif choice == "3":
                self.job_portal(user)
            elif choice == "4":
                self.check_progress(user)
            elif choice == "5":
                self.display_notifications()
            elif choice == "6":
                print(f"Thank you for exploring Smart Farming. Have a great day!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    platform = SmartFarmingPlatform()
    platform.main()
