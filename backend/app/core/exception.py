
class EmailAlreadyExists(Exception):
    def __init__(self):
        super().__init__(f"Email is already registered.")