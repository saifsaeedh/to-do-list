import json

class Task:
    def __init__(self, id: int, title: str, description: str, complete: bool, priority: str):
        self.id = id
        self.title = title
        self.description = description
        self.complete = complete
        self.priority = priority

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "complete": self.complete,
            "priority": self.priority
        }
    
    #def from_dict(self):


