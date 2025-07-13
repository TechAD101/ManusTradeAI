
class User:
    """Mock User model."""
    _users = [] # In-memory storage for demonstration

    def __init__(self, username, password, role="trial"):
        self.id = len(User._users) + 1
        self.username = username
        self.password = password # In a real app, this would be hashed
        self.role = role

    def save(self):
        User._users.append(self)

    @classmethod
    def find_by_username(cls, username):
        for user in cls._users:
            if user.username == username:
                return user
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }


