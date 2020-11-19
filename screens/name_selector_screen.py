from screens.screen import Screen
from screens.shop_screen import ShopScreen
import pygame
import util
from wagon import Wagon


class NameSelectorScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    self.names = ["", "", "", "", "", ""]
    self.selected = 0
    print("Name selector screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    # ? These pygame.image.load calls are costly. Maybe put them into constants?
    img1 = pygame.image.load("screens/assets/mama.png")
    img2 = util.imgscale(pygame.image.load("screens/assets/gunman.png"), 1.5)
    img3 = util.imgscale(pygame.image.load("screens/assets/oxen.png"), 1.5)
    img4 = util.imgscale(pygame.image.load("screens/assets/wagon.png"), 3)
    screen.blit(img1, (50, 80))
    screen.blit(img2, (350, 90))
    screen.blit(img4, (200, 80))
    screen.blit(img3, (170, 110))
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
    elif len(self.names[self.selected]) < 12 and util.is_letter(key):
      charKey = str(chr(key))
      mods = pygame.key.get_mods()
      if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT] or mods & pygame.KMOD_CAPS:
        charKey = charKey.upper()
      if not self.selected == 5:
        self.names[self.selected] += charKey
      else:
        if charKey == "y":
          self.names.pop()
          people = util.array_to_person(self.names)
          self.data["wagon"] = Wagon(people, people[0])
          self.next = ShopScreen(self.data)
          self.idle = True
        elif charKey == "n":
          self.names = ["", "", "", "", "", ""]
          self.selected = 0

  def render_multiline_field(self, text, entered, x, y, screen, selected):
    font = pygame.font.Font('font/font.ttf', 17)
    if entered == "" and selected:
      text += "_"
    else:
      text += entered
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 17 * i))