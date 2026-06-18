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
    task = Task(next_id, title, description, False, priority)
    logger.debug("Task was created")
    return task

def add_task(task):
    with open ("tasks.json", "r") as file:
        tasks = json.load(file)
    
    tasks.append(task.to_dict())
    logger.info("Task added to tasks.json")

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id():
    with open ("tasks.json", "r") as file:
        tasks = json.load(file)
        if not tasks:
            return 1
    return tasks[-1]["id"] +1

def remove_task():
    logger.info("Task removed")

def view_tasks():
    logger.info("Tasks viewed")

def find_task():
    logger.info("Task found")