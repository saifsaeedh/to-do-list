import menu
import logger
import manager
import json

from task import Task

from logger import logger

def initializer():
    with open("tasks.json", "a+") as file:
        file.seek(0)

        if file.read() == "":
            file.write("[]")
        logger.info("To-do app initialized")

while True:
    initializer()
    menu.show_main()
    manager.load_tasks()
    break