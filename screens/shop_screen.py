from screens.screen import Screen
import util
import pygame

class ShopScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    self.bill = {"oxen": 0, "food": 0, "clothing": 0, "ammunition": 0, "spare_parts": 0}
    self.money = data["wagon"].inventory["cash"]
    self.showScreen = 0
    self.input = [""]
    print("Shop screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 15)
    shopImage = pygame.image.load("screens/assets/shop.png")
    screen.blit(shopImage, (0, 0))
    # IMPORTANT: you can also buy spare wagon parts
    if self.showScreen == 0:
      space = font.render('Press SPACE to continue.', True, WHITE)
      screen.blit(space, (75, 475))
      self.render_multiline("Before leaving, you should\nbuy equipment and supplies.\nYou have $"+str(self.money)+"0 in cash,\nbut you don't have to\nspend it all now.", 20, 10, screen)
    elif self.showScreen == 1:
      space = font.render('Press SPACE to continue.', True, WHITE)
      screen.blit(space, (75, 475))
      self.render_multiline("You can buy whatever you\nneed at Matt's General\nStore.", 20, 10, screen)
    elif self.showScreen == 2:
      self.render_multiline('Shop: \n 1. Oxen \n 2. Food \n 3. Clothes\n 4. Ammo\n 5. Spare parts', 225, 20, screen)
    elif self.showScreen == 3:
      self.render_multiline("Oxen:\n They're there to ride \n your wagon across \n the trail!", 50, 20, screen)
    elif self.showScreen == 4:
      self.render_multiline("Food:\n You'll need a lot of \n food for the trip!", 50, 20, screen)
    elif self.showScreen == 5:
      self.render_multiline("Clothes:\n You'll need them\n for the cruel winters!", 50, 20, screen)
    elif self.showScreen == 6:
      self.render_multiline("Ammo:\n Use it if your in trouble \n or just need to hunt \n for some game.", 50, 20, screen)
    elif self.showScreen == 7:
      self.render_multiline("Spare parts:\n You'll need this in case your\n wagon breaks down!", 50, 20, screen)
    
    if self.showScreen > 2 and self.showScreen < 7:
      options = ["many\nyokes (pairs)", "many pounds", "many\nsets", "many boxes of 20"]
      self.render_multiline_field("How " + options[self.showScreen - 3] + " would\nyou like to\npurchase? ", self.input[0], 225, 150, screen, True)

  def process_input(self, key):
    if key == pygame.K_RETURN:
      if self.showScreen > 2 and self.showScreen < 7:
        items = ["oxen", "food", "clothing", "ammunition", "spare_parts"]
        self.bill[items[self.showScreen - 3]] = self.input[0]
        self.input[0] = ""
        self.showScreen = 2
    elif util.is_letter(key):
      charKey = str(chr(key))
      if self.showScreen < 2 and charKey == " ":
        self.showScreen += 1
      if self.showScreen > 2 and self.showScreen < 7:
        self.input[0] += charKey
      elif str(charKey) == '1':
        self.showScreen = 3
        print(self.showScreen)
      elif str(charKey) == '2':
        self.showScreen = 4
      elif str(charKey) == '3':
        self.showScreen = 5
      elif str(charKey) == '4':
        self.showScreen = 6
      elif str(charKey) == '5':
        self.showScreen = 7
          

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))

  def isNumber(self, number):
    try:
      int(number)
      return True
    except:
      return False

  def render_multiline_field(self, text, entered, x, y, screen, selected):
    font = pygame.font.Font('font/font.ttf', 17)
    if entered == "" and selected:
      text += "_"
    else:
      text += entered
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 17 * i))