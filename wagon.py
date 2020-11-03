from typing import Union, Any
from date import Date
from person import Person
from enum import Enum

# Wagon class
# Author: Seamus Smith                          ( ´･･)ﾉ┻━┻
#                                               ‾‾‾‾‾ ᓚᘏᗢ
#                                                    	‾‾‾‾
class Wagon:
  class DamagedPart(Enum):
    AXEL = 0
    WHEEL = 1
    TONGUE = 3
  def __init__(self, party: list, main_character: Person):
    self.inventory: dict = {
      "food": 0,
      "cash": 0,
      "clothing": 0,
      "ammunition": 0,
      "axel": 0,
      "wheel": 0,
      "tongues": 0
    }
    self.main_character = main_character
    self.damaged: bool = False
    self.damaged_part: Any
    self.oxen: list = []
    self.party: list = []
  #update all party members
  def update_party(self) -> None:
    for i in self.party:
      i.update() if i.alive else (0)
  # update oxen
  def update_oxen(self) -> None:
    for ox, i in enumerate(self.oxen):
      ox.update() if ox.alive else self.oxen.remove(i)
  def update_wagon(self) -> None:
    raise NotImplementedError("the wagon crashed, burned, and blew up")
    # should probably be a chance to damage the wagon, requiring spare parts

