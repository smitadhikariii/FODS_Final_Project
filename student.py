from file_manager import FileManager
from user import User
from colorama import Fore

# This class handles student features
class Student(User):
    def menu(self):
        # Show student-specific menu
        while True:
            print(Fore.CYAN + "\n--- Student Menu ---")
            print("1. View profile")
            print("2. Update profile")
            print("3. View grades")
            print("4. View ECA participation")
            print("5. Join/Update ECA")
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_profile()
            elif choice == '2':
                self.update_profile()
            elif choice == '3':
                self.view_grades()
            elif choice == '4':
                self.view_eca()
            elif choice == '5':
                self.join_eca()
            elif choice == '6':
                print(Fore.YELLOW + "You have successfully logged out!")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")

    def view_profile(self):
        # Show student profile from file
        users = FileManager.read_file("users.txt")
        for line in users:
            if line.startswith(self.username + ","):
                print("Profile:", line)
                return

    def update_profile(self):
        # Allow student to update their name and email
        users = FileManager.read_file("users.txt")
        for i, line in enumerate(users):
            if line.startswith(self.username + ","):
                parts = line.split(",")
                name = input(f"New name (current: {parts[1]}): ")
                email = input(f"New email (current: {parts[2]}): ")
                users[i] = f"{self.username},{name},{email},student"
                FileManager.write_file("users.txt", users)
                print("Profile updated.")
                return

    def view_grades(self):
        # Show grades for the student
        grades = FileManager.read_file("grades.txt")
        for line in grades:
            if line.startswith(self.username + ","):
                parts = list(map(int, line.split(",")[1:]))
                subjects = ["Math", "English", "Science", "History", "CompSci"]
                for sub, mark in zip(subjects, parts):
                    print(f"{sub}: {mark}")
                return

    def view_eca(self):
        # Display ECA activities student has joined
        eca = FileManager.read_file("eca.txt")
        for line in eca:
            if line.startswith(self.username + ","):
                activities = line.split(",")[1:]
                print("ECA Participation:", ", ".join(activities))
                return

    def join_eca(self):
        # Allow student to select ECAs to join (adds to existing)
        choices = ["Football", "Table Tennis", "Badminton", "Cricket", "Debate"]
        print("Available ECAs:")
        for idx, choice in enumerate(choices, 1):
            print(f"{idx}. {choice}")
        selected = input("Enter the numbers of ECAs to join (comma-separated): ")
        try:
            indexes = list(map(int, selected.split(",")))
            selected_activities = [choices[i - 1] for i in indexes]
            eca = FileManager.read_file("eca.txt")
            for i, line in enumerate(eca):
                if line.startswith(self.username + ","):
                    existing = line.split(",")[1:]
                    updated = list(set(existing + selected_activities))
                    eca[i] = f"{self.username}," + ",".join(updated)
                    FileManager.write_file("eca.txt", eca)
                    print("ECA updated.")
                    return
        except Exception as e:
            print("Invalid selection.")
