import menu
import logger
import manager
from task import Task

from logger import logger

def get_choice():
    choice = input("Enter choice: ")
    logger.debug(f"User entered choice {choice}")
    return choice

def initializer():
    with open("tasks.json", "a+") as file:
        file.seek(0)

        if file.read() == "":
            file.write("[]")
        logger.info("To-do app initialized")

while True:
    initializer()
    menu.show_main()
    choice = get_choice()
    if choice in ["1", "2", "3", "4"]:
        if choice == "1":
            data = []
            data = manager.load_tasks()
            manager.view_tasks(data)

        elif choice == "2":
            task = manager.create_task(manager.get_next_id())
            manager.add_task(task)
        elif choice == "3":
            manager.remove_task()
        elif choice == "4":
            manager.find_task()
    else:
        print("Invalid choice, try again")    
    break