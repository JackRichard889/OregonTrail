from itembaseclass import BaseItem

class TestItem(BaseItem):
  stackable_size = 99
  def __init__(self):
    pass
  def interact(self):
    print("Wowie!!!")