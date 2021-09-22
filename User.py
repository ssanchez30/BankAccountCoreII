class User:
    def __init__(self, firstname="N/A", lastname="N/A", email="N/A"):
        self.firstName = firstname
        self.lastName = lastname
        self.email = email

    def printUserInfo(self):
        print(
            f"First name: {self.firstName}\nLast name: {self.lastName}\nEmail: {self.email}")
