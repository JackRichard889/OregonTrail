from items import *
from itembaseclass import BaseItem
from typing import Union

class ItemStack():
  def __init__(self, itemtype: BaseItem, max_size: int, count: int = 0):
    self.__max_size = max_size
    self.__itemtype = itemtype
    self.__item_count = count
  def add_items(self, count: int) -> bool:
    if self.__item_count + count > self.__max_size:
      return False
    else:
      self.__item_count += count
    return True
  def take_from_stack(self) -> Union[type, None]:
    if self.__item_count > 0:
      return self.__itemtype
    else:
      return None
  def get_type(self):
    return self.__itemtype
