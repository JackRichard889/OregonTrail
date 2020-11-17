from screens.screen import Screen
import util
import pygame

class ShopScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    self.items = [""]
    self.money = 1600
    print("Shop screen created.")

  def render(self, screen):
    screen_show = 0

    if screen_show == 0:
      WHITE = (255, 255, 255)
      background = (0, 0, 0)
      screen.fill(background)
      font = pygame.font.Font('font/font.ttf', 29)
      shopImage = pygame.image.load("screens/assets/shop.png")
      screen.blit(shopImage, (0, 0))
      self.render_multiline('Shop: \n1.Oxen \n2.Food \n3.Clothes\n4.Ammo', 300, 20, screen)

    elif screen_show == 'Oxen':
      font = pygame.font.Font('font/font.ttf', 29)
      txt_Oxen = font.render('OXXX', 120, 20, screen)  
      screen.blit(txt_Oxen, (25, 100))    

  def process_input(self, key):
    if util.is_letter(key):
      charKey = str(chr(key))

    if int(charKey) == 1:
      screen_show = 'Oxen'
      print(screen_show)

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))
