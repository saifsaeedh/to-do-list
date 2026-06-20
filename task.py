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
    
    @classmethod
    def from_dict(cls, task_data):
        return cls(
            id=task_data["id"], 
            title=task_data["title"], 
            description=task_data["description"], 
            complete=task_data["complete"], 
            priority=task_data["priority"]
            )


