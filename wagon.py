from typing import Union
from itembaseclass import BaseItem
from itemstack import ItemStack
from date import Date

class Wagon:
  def __init__(self, party: list):
    self.inventory: dict = {
      "food": 0,
      "cash": 0,
      "clothing": 0,
      "ammunition": 0,
      "axel": 0,
      "wheel": 0
    }
    self.oxen: list = []
    self.party: list = []
  def update_party(self, d: Date):
    for i in self.party:
      i.update()
