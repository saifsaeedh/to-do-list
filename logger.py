import logging
 
from logging import FileHandler
from logging import Formatter

logger = logging.getLogger("todo_app")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
    )

handler = FileHandler("todo.log")

handler.setFormatter(formatter)

logger.addHandler(handler)