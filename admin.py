from file_manager import FileManager
from user import User
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore

# This class handles admin functionalities
class Admin(User):
    def menu(self):
        # Display admin options
        while True:
            print(Fore.GREEN + "\n--- Admin Menu ---")
            print("1. Add new student")
            print("2. Update student record")
            print("3. Delete student record")
            print("4. View student list")
            print("5. Generate insights")
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.view_students()
            elif choice == '5':
                self.generate_insights()
            elif choice == '6':
                print(Fore.YELLOW + "You have successfully logged out!")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")

    def add_student(self):
        # Collect and add new student details
        username = input("Enter new student username: ")
        name = input("Full name: ")
        email = input("Email: ")
        role = "student"

        # Check if username already exists
        users = FileManager.read_file("users.txt")
        if any(username in line for line in users):
            print("Username already exists.")
            return

        # Append new student data to files
        FileManager.append_to_file("users.txt", f"{username},{name},{email},{role}")
        FileManager.append_to_file("passwords.txt", f"{username},1234")
        FileManager.append_to_file("grades.txt", f"{username},0,0,0,0,0")
        FileManager.append_to_file("eca.txt", f"{username},none")
        print("Student added successfully!")

    def update_student(self):
        # Update name and email of existing student
        username = input("Enter student username to update: ")
        users = FileManager.read_file("users.txt")
        updated = False

        for i, line in enumerate(users):
            parts = line.split(",")
            if parts[0] == username:
                name = input(f"New name (current: {parts[1]}): ")
                email = input(f"New email (current: {parts[2]}): ")
                users[i] = f"{username},{name},{email},student"
                updated = True
                break

        if updated:
            FileManager.write_file("users.txt", users)
            print("Student record updated.")
        else:
            print("Student not found.")

    def delete_student(self):
        # Remove student info from all related files
        username = input("Enter student username to delete: ")
        for fname in ["users.txt", "passwords.txt", "grades.txt", "eca.txt"]:
            lines = FileManager.read_file(fname)
            lines = [line for line in lines if not line.startswith(username + ",")]
            FileManager.write_file(fname, lines)
        print("Student record deleted.")

    def view_students(self):
        # Print a list of all students
        print("\nRegistered Students:")
        users = FileManager.read_file("users.txt")
        for user in users:
            parts = user.split(",")
            if parts[3] == "student":
                print(f"- {parts[1]} ({parts[0]}, {parts[2]})")

    def generate_insights(self):
        # Show average grades and ECA participation stats
        print(Fore.MAGENTA + "\n--- Data Insights ---")
        try:
            df = pd.read_csv("grades.txt", header=None)
            df.columns = ["Username", "Math", "English", "Science", "History", "CompSci"]
            subjects = df.columns[1:]
            avg = df[subjects].mean()
            print("Average grades per subject:")
            for subj in subjects:
                print(f"{subj}: {avg[subj]:.2f}")

            plt.bar(subjects, avg)
            plt.title("Average Grades per Subject")
            plt.ylabel("Average Marks")
            plt.show()
        except Exception as e:
            print("Could not generate chart:", e)

        # Count ECA participation
        eca_lines = FileManager.read_file("eca.txt")
        activity_count = {}
        for line in eca_lines:
            parts = line.split(",")[1:]
            for activity in parts:
                if activity != "none":
                    activity_count[activity] = activity_count.get(activity, 0) + 1

        if activity_count:
            print("\nMost active ECA participants:")
            for act, cnt in activity_count.items():
                print(f"{act}: {cnt}")
