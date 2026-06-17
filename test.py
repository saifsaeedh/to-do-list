import menu
import logger
import manager
import json

from task import Task

from logger import logger

def get_choice():
    choice = input("Enter choice: ")
    logger.debug(f"User entered choice {choice}")
    return choice

def initializer():
    with open("tasks.json", "a") as file:
        logger.info("Calculator initialized")
        logger.info("JSON file is loaded/created")
        pass

#def id_counter():
#    with open("")

while True:
    initializer()
    menu.show_main()
    choice = get_choice()
    if choice in ["1", "2", "3", "4"]:
        if choice == "1":
            task = manager.create_task()
            manager.add_task(task)
        elif choice == "2":
            manager.remove_task()
        elif choice == "3":
            manager.view_tasks()
        elif choice == "4":
            manager.find_task()
    elif choice == "0":
        logger.info("Program has shut down")
        break
    
    else:
        print("Invalid choice, try again")
    

    break