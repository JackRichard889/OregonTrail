from typing import Union, Any
from date import Date
from person import Person
from enum import Enum
from environment import Environment
import util

#                                    |squinch time|
# Wagon class                            /
# Author: Seamus Smith               ( ´･･)ﾉ┻━┻
#                                    ‾‾‾‾‾ ᓚᘏᗢ
#                                    ‾‾‾‾‾‾‾‾‾‾‾

class Wagon:
  class DamagedPart(Enum):
    NONE = 0
    AXEL = 1
    WHEEL = 2
    TONGUE = 3
  def __init__(self, party: list, main_character: Person):
    self.inventory: dict = {
      "food": 0,
      "cash": util.money_for_profession(main_character.occupation),
      "clothing": 0,
      "ammunition": 0,
      "axel": 0,
      "wheel": 0,
      "tongue": 0
    }
    self.main_character: Person = main_character
    self.damage: Wagon.DamagedPart = Wagon.DamagedPart.NONE
    self.oxen: list = []
    self.party: list = party
  #update all party members
  def update_party(self) -> None:
    for i in self.party:
      i.update() if i.alive else (0)
  # update oxen
  def update_oxen(self) -> None:
    for ox, i in enumerate(self.oxen):
      ox.update() if ox.alive else self.oxen.remove(i)
  def update_wagon(self, env: Environment) -> None:
    raise NotImplementedError("the wagon crashed, burned, and blew up")
    # should probably be a chance to damage the wagon, requiring spare parts

