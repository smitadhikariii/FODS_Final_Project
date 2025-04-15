# This is the base class for all users
class User:
    def __init__(self, username):
        self.username = username

    def menu(self):
        # Child classes like Admin and Student will define their own menu
        raise NotImplementedError("Subclasses must implement this method")
