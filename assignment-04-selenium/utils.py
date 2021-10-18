from typing import Callable
from time import sleep

def delay(fn: Callable) -> Callable:
   def wrapper():
      fn()
      sleep(4)

   return wrapper