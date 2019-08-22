from config import *

def parse_command(string):
    return string[len(prefix):].split()
