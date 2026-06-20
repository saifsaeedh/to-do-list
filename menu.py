import logger
from logger import logger

def show_main():
    print("This is a basic to-do list app")
    print()
    print("Select an operation")
    print()
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove Tasks")
    print("4. Find tasks")
    print()
    print("0. Quit program")
    print()
    logger.info("Menu shown")