from screens.screen import Screen
from screens.shop_screen import ShopScreen
import pygame
import util


class NameSelectorScreen(Screen):
  def __init__(self):
    self.names = ["", "", "", "", "", ""]
    self.selected = 0
    print("Name selector screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    img1 = pygame.image.load("screens/assets/mama.png")
    img2 = pygame.image.load("screens/assets/gunman.png")
    img3 = pygame.image.load("screens/assets/oxen.png")
    img4 = pygame.image.load("screens/assets/wagon.png")
    screen.blit(img1, (50, 125))
    screen.blit(img2, (100, 125))
    screen.blit(img3, (150, 125))
    screen.blit(img4, (200, 125))
    font = pygame.font.Font('font/font.ttf', 29)
    title = font.render('The Oregon Trail', True, WHITE)
    self.render_multiline_field('What is the first name of\nthe wagon leader? ', self.names[0], 25, 240, screen, self.selected == 0)
    font = pygame.font.Font('font/font.ttf', 17)
    if self.selected > 0:
      for i in range(4):
        self.render_multiline_field("#"+str(i+2)+": ",self.names[i+1], 25, 300+(i*30), screen, self.selected == i+1)
    screen.blit(title, (24, 40))
    if self.selected == 5:
      self.render_multiline_field("Are these names correct? ", "", 25, 475, screen, True)

  def process_input(self, key):
    if key == pygame.K_RETURN:
      if self.selected < 4:
        self.selected += 1
      else:
        self.selected = 5
    elif key == pygame.K_BACKSPACE:
      if len(self.names[self.selected]) > 0:
        self.names[self.selected] = self.names[self.selected][:-1]
    elif len(self.names[self.selected]) < 12 and self.is_letter(key):
      charKey = str(chr(key))
      mods = pygame.key.get_mods()
      if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT] or mods & pygame.KMOD_CAPS:
        charKey = charKey.upper()
      if not self.selected == 5:
        self.names[self.selected] += charKey
      else:
        if charKey == "y":
          return ShopScreen()
        elif charKey == "n":
          self.names = ["", "", "", "", "", ""]
          self.selected = 0
    return self
  def render_multiline_field(self, text, entered, x, y, screen, selected):
    font = pygame.font.Font('font/font.ttf', 17)
    if entered == "" and selected:
      text += "_"
    else:
      text += entered
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 17 * i))
  def is_letter(self, i):
    try: 
        chr(i)
        return True
    except ValueError:
        return False