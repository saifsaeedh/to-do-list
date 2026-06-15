class Task:
    def __init__(self, title: str, description: str, is_complete: bool, priority: str):
        self.title = title
        self.description = description
        self.is_complete = is_complete
        self.priority = priority