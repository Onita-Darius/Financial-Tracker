
class EmailAlreadyExists(Exception):
    def __init__(self):
        super().__init__(f"Email is already registered.")

class InvalidUser(Exception):
    def __init__(self, *args):
        super().__init__(f"Invalid user credentials")

class InvalidToken(Exception):
    def __init__(self, *args):
        super().__init__(f"Invalid Access Token")