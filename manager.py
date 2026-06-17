from logger import logger
from task import Task

def create_task():
    title = input("Enter task title: ")
    logger.debug(f"User typed {title} for task title")
    description = input("Enter task description: ")
    logger.debug(f"User typed {description} for task description")
    priority = input("Choose task priority from 1 to 3: ")
    logger.debug(f"User choice {priority} for task priority")
    task = Task(id, title, description, False, priority)
    logger.debug("Task was created")
    return task

def add_task(entry):
    with open ("tasks.txt", "a") as file:
        lines = file.write(f"Title: {entry.title}\nDescription: {entry.description}\nCompleted: {entry.is_complete}\nPriority: {entry.priority}")    
        logger.info("Task added")


def remove_task():
    logger.info("Task removed")

def view_tasks():
    logger.info("Tasks viewed")

def find_task():
    logger.info("Task found")