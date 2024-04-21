
from os import path
from datetime import datetime


def addlog(text, data):
    with open(path.dirname(path.abspath(__file__))+"/log.txt", "a") as file:
        file.write(text)
        file.write(
            f"\n-----------------error in {data} on {datetime.now()}\n\n\n")
