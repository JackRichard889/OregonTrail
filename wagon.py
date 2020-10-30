from typing import union

class Wagon:
  def __init__(self, inventory_size: int):
    self.inventory: list = []
    self.__max_inventory_size: int = inventory_size
    self.oxen: list = []
    self.party: list = []
  
  pass

class ItemStack():
  def __init__(self, itemtype: type, max_size: int):
    self.max_size = max_size
    self.itemtype = itemtype
  