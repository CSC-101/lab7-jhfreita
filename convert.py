import math
from typing import Optional
def str_to_float(string):
    try:
        return float(string)
    except ValueError:
        return None
print(str_to_float('4'))