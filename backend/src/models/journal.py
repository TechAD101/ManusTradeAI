
from datetime import datetime

class JournalEntry:
    """Mock JournalEntry model."""
    _entries = [] # In-memory storage for demonstration

    def __init__(self, title, content, user_id):
        self.id = len(JournalEntry._entries) + 1
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = datetime.now()

    def save(self):
        JournalEntry._entries.append(self)

    @classmethod
    def find_by_user_id(cls, user_id):
        return [entry for entry in cls._entries if entry.user_id == user_id]

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat()
        }


