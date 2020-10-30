from typing import Union

class Wagon:
  def __init__(self, inventory_size: int):
    self.inventory: list = []
    self.__max_inventory_size: int = inventory_size
    self.oxen: list = []
    self.party: list = []
  def add_item(self) -> bool:
    pass
  def find_item() -> bool:
    pass
  def take_item() -> bool:
    pass
  pass

class ItemStack():
  def __init__(self, itemtype: type, max_size: int, count: int = 0):
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

class TestItem():
  pass