import os
from .start import start
from pathlib import Path

# variables
ignore_set = {'__init__.py','__pycache__'} # set of files to ignore
file_list = os.listdir('./commands')

# list of commands objects
commands = [globals()[Path(file).stem] for file in file_list if file not in ignore_set]
