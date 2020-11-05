from screens.screen import Screen
import util
import pygame

class ShopScreen(Screen):
  def __init__(self, data):
    self.data = data
    print(data)
    print("Shop screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 29)
    shopImage = pygame.image.load("screens/assets/shop.png")
    screen.blit(shopImage, (0, 0))
  def process_input(self, key):
    if util.is_letter(key):
      charKey = str(chr(key))
    return self

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))