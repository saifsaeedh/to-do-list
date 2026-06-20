from logger import logger
from task import Task
import json

def create_task(next_id):
    title = input("Enter task title: ")
    logger.debug(f"User typed {title} for task title")
    description = input("Enter task description: ")
    logger.debug(f"User typed {description} for task description")
    priority = input("Choose task priority from 1 to 3: ")
    logger.debug(f"User choice {priority} for task priority")
    new_task = Task(next_id, title, description, False, priority)
    logger.debug("Task was created")
    return new_task

def add_task(task):
    with open ("tasks.json", "r") as file:
        data = json.load(file)
    
    data.append(task.to_dict())
    logger.info("Task added to tasks.json")

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

def get_next_id():
    with open ("tasks.json", "r") as file:
        tasks = json.load(file)
        if not tasks:
            return 1
    return tasks[-1]["id"] +1

def load_tasks():
    with open ("tasks.json", "r") as file:
        data = json.load(file)
        if not data:
            print("No tasks saved")
            return []
    
        tasks = []

        for task_data in data:
            tasks.append(Task.from_dict(task_data))
        return tasks

    logger.info("Tasks loaded")

def view_tasks(data):
    for task in data:
                print()
                print(f"ID: {task.id}")
                print(f"Task title: {task.title}")
                print(f"Task description: {task.description}")
                print(f"Task priority: {task.priority}")
                print()

def remove_task():
    logger.info("Task removed")

def find_task():
    logger.info("Task found")