import time

class User:
    def __init__(self, name):
        self.name = name
        self.progress = {"Educational Modules": 0, "Q&A Sessions": 0, "Job Applications": 0}

class SmartFarmingPlatform:
    def __init__(self):
        self.users = {}
        self.notifications = []

    def introduction(self):
        print("Welcome to the Smart Farming Platform!")
        print("Our mission is to empower farmers through education, collaboration, and employment opportunities.")
        print("Let's embark on this journey together!\n")

    def start_prompt(self):
        while True:
            choice = input("Are you ready to explore Smart Farming? (yes/no): ").lower()

            if choice == "yes":
                print("\nGreat! Let's get started.")
                break
            elif choice == "no":
                print("Alright, feel free to return whenever you're ready.")
                exit()
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

    def educational_module(self, user):
        print("\n=== Educational Modules ===")
        print("1. Modern Farming Techniques")
        print("2. Sustainable Practices")
        choice = input("Enter the number of the module you want to explore: ")

        if choice == "1":
            print("\n=== Modern Farming Techniques ===")
            print("Check out the following resources:")
            print("1. Article: Introduction to Precision Agriculture - https://extension.missouri.edu/publications/wq450")
            print("2. Video: Advanced Irrigation Techniques - https://youtu.be/Z9HAy9EYKKs?feature=shared")
            user.progress["Educational Modules"] += 1
        elif choice == "2":
            print("\n=== Sustainable Practices ===")
            print("Explore the following materials:")
            print("1. Article: Sustainable Crop Rotation Strategies - https://sustainablereview.com/sustainable-crop-rotation-practices/")
            print("2. Video: Organic Farming Methods - https://youtu.be/WhOrIUlrnPo?feature=shared")
            user.progress["Educational Modules"] += 1
        else:
            print("Invalid choice. Please enter a valid module number.")

    def qna_interaction(self, user):
        print("\n=== Live Q&A ===")
        question = input("Ask a question to the agricultural experts: ")
        print(f"Thank you for your question, {user.name}! Our experts will respond shortly.")
        user.progress["Q&A Sessions"] += 1

    def job_portal(self, user):
        print("\n=== Job Portal ===")
        print("1. Agricultural Specialist - Company A")
        print("2. Farm Manager - Company B")
        choice = input("Enter the number of the job you want to apply for: ")

        if choice in ["1", "2"]:
            print(f"Congratulations, {user.name}! You've applied for a job. Good luck!")
            user.progress["Job Applications"] += 1
        else:
            print("Invalid choice. Please enter a valid job number.")

    def check_progress(self, user):
        print("\n=== Progress Tracking ===")
        print(f"Hello {user.name}! Your progress so far:")
        for category, progress in user.progress.items():
            print(f"{category}: {progress}")

    def display_notifications(self):
        print("\n=== Notifications ===")
        for notification in self.notifications:
            print(notification)

    def main(self):
        self.introduction()
        self.start_prompt()

        while True:
            username = input("Enter your name: ")
            if username not in self.users:
                self.users[username] = User(username)

            user = self.users[username]

            self.display_dashboard()
            choice = input("\nEnter the number of your choice: ")

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
                print(f"Thank you, {user.name}, for exploring Smart Farming. Have a great day!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    platform = SmartFarmingPlatform()
    platform.main()
