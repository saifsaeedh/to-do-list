import logger
from logger import logger

def show_main():
    print("This is a basic to-do list app")
    print()
    print("Select an operation")
    print()
    print("1. Add task")
    print("2. Remove task")
    print("3. View Tasks")
    print("4. Find tasks")
    print()
    print("0. Quit program")
    print()
    logger.info("Menu shown")