
class EmailAlreadyExists(Exception):
    def __init__(self, email: str):
        super().__init__(f"Email '{email}' is already registered.")