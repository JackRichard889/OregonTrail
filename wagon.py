from typing import Union
from itembaseclass import BaseItem
from itemstack import ItemStack

class Wagon:
  def __init__(self, inventory_size: int, party: list):
    self.__inventory: Inventory = Inventory(inventory_size)
    self.__max_inventory_size: int = inventory_size
    self.__oxen: list = []
    self.__party: list = []
  def add_item(self) -> bool:
    pass
  def find_item(self) -> bool:
    pass
  def take_item(self) -> bool:
    pass

class Inventory():
  def __init__(self, size: int):
    self.__size: int = size
    self.__items: set = set()
  # Returns true on item addition success, false on failure (stack too large)
  def add_items(self, item: BaseItem, count: int) -> bool:
    for stack in self.__items:
      if stack.get_type() == item:
        return stack.add_items(count)
    self.__items.add(ItemStack(item, item.stackable_size, count))
    return True
  #todo