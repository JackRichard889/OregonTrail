from screens.screen import Screen
import util
import pygame

class ShopScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    self.money = data["wagon"].inventory["cash"]
    self.showScreen = 0
    print("Shop screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 29)
    shopImage = pygame.image.load("screens/assets/shop.png")
    screen.blit(shopImage, (0, 0))
    if self.showScreen == 0:
      self.render_multiline('Shop: \n 1.Oxen \n 2.Food \n 3.Clothes\n 4.Ammo', 300, 20, screen)
      self.render_multiline_field("Amount: ", )
    elif self.showScreen == 1:
      self.render_multiline("Oxen: \n They're there to ride \n your wagon across \n the trail!", 50, 20, screen)
    elif self.showScreen == 2:
      self.render_multiline("Food: \n You'll need a lot o)f \n food for the trip!", 50, 20, screen)
    elif self.showScreen == 3:
      self.render_multiline("Clothes: \n You'll need them\n for the cruel winters! ", 50, 20, screen)
    elif self.showScreen == 4:
      self.render_multiline("Ammo: \n Use it if your in trouble \n or just need to \n hunt for some game", 50, 20, screen)

  def process_input(self, key):
    if util.is_letter(key):
      charKey = str(chr(key))
      if str(charKey) == '1':
        self.showScreen = 1
        print(self.showScreen)
      if str(charKey) == '2':
        self.showScreen = 2
      if str(charKey) == '3':
        self.showScreen = 3
      if str(charKey) == '4':
        self.showScreen = 4
          

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