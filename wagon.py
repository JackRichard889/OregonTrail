from typing import Union
from itembaseclass import BaseItem
from itemstack import ItemStack

class Wagon:
  def __init__(self, party: list):
    self.inventory: dict = {
      "food": 0,
      "cash": 0,
      "clothing": 0
    }
    self.oxen: list = []
    self.party: list = []
