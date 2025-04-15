from file_manager import FileManager
from admin import Admin
from student import Student
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Ask for login info and return the appropriate user object
def login():
    print(Fore.CYAN + "--- Login ---")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        creds = FileManager.read_file("passwords.txt")
        for line in creds:
            user, pw = line.split(",")
            if user == username and pw == password:
                users = FileManager.read_file("users.txt")
                for u in users:
                    if u.startswith(username + ","):
                        role = u.split(",")[3]
                        return Admin(username) if role == "admin" else Student(username)
        print(Fore.RED + "Invalid credentials. Try again.")

# Entry point of the program
def main():
    print(Fore.CYAN + "Welcome to the Student Profile Management System")
    user = login()
    user.menu()

if __name__ == "__main__":
    main()

