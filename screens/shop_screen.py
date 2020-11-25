from screens.screen import Screen
from screens.alert_screen import AlertScreen
from screens.splash_screen import SplashScreen
from screens.trail.options_screen import OptionsScreen
from environment import Landmarks
import util
import pygame

class ShopScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    self.bill = {"oxen": 0, "food": 0, "clothing": 0, "ammunition": 0, "spare_parts": {"wheel": 0, "axel": 0,"tongue": 0}}
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
    
    if self.showScreen == 0:
      space = font.render('Press SPACE to continue.', True, WHITE)
      screen.blit(space, (75, 475))
      self.render_multiline("Before leaving, you should\nbuy equipment and supplies.\nYou have $"+str(self.money)+"0 in cash,\nbut you don't have to\nspend it all now.", 20, 10, screen)
    elif self.showScreen == 1:
      space = font.render('Press SPACE to continue.', True, WHITE)
      screen.blit(space, (75, 475))
      self.render_multiline("You can buy whatever you\nneed at Matt's General\nStore.", 20, 10, screen)
    elif self.showScreen == 2:
      space = font.render('Press SPACE to leave.', True, WHITE)
      screen.blit(space, (95, 475))
      self.render_multiline('Shop: \n 1. Oxen \n 2. Food \n 3. Clothes\n 4. Ammo\n 5. Spare parts', 205, 50, screen)
    elif self.showScreen == 3:
      self.render_multiline("Oxen:\n They're there to ride \n your wagon across \n the trail!", 50, 20, screen)
    elif self.showScreen == 4:
      self.render_multiline("Food:\n You'll need a lot of \n food for the trip!", 50, 20, screen)
    elif self.showScreen == 5:
      self.render_multiline("Clothes:\n You'll need them\n for the cruel winters!", 50, 20, screen)
    elif self.showScreen == 6:
      self.render_multiline("Ammo:\n Use it if you're in\n trouble or just need to\n hunt for some game.", 50, 20, screen)
    elif self.showScreen >= 7 and self.showScreen <= 9:
      self.render_multiline("Spare parts:\n You'll need these in case your\n wagon breaks down!", 50, 20, screen)
      options = ["wheels", "axels", "tongues"]
      self.render_multiline_field("How many " + options[self.showScreen - 7] + " \nwould you like to\npurchase? ", self.input[0], 215, 150, screen, True)
    
    if self.showScreen > 2 and self.showScreen < 7:
      options = ["many yokes\n(pairs)", "many pounds", "many\nsets", "many boxes\nof 20"]
      self.render_multiline_field("How " + options[self.showScreen - 3] + " would\nyou like to\npurchase? ", self.input[0], 225, 150, screen, True)

  def process_input(self, key):
    if key == pygame.K_RETURN:
      if self.showScreen > 2 and self.showScreen < 7 and self.isNumber(self.input[0]):
        items = ["oxen", "food", "clothing", "ammunition", "spare_parts"]
        if int(self.input[0]) > self.get_max(self.showScreen - 3):
          self.next = AlertScreen(self.data, "You can only hold "+str(self.get_max(self.showScreen - 3))+"\nof this item.")
        else:
          self.bill[items[self.showScreen - 3]] = int(self.input[0])
          self.input[0] = ""
          self.showScreen = 2
      elif self.showScreen >= 7 and self.showScreen <= 9 and self.isNumber(self.input[0]):
        items = ["wheel", "axel", "tongue"]
        if int(self.input[0]) > 3:
          self.next = AlertScreen(self.data, "You can only hold\n3 of these.")
        else:
          self.bill["spare_parts"][items[self.showScreen - 7]] = int(self.input[0])
          self.input[0] = ""
          self.showScreen += 1
          if self.showScreen > 9:
            self.showScreen = 2
    elif key == pygame.K_BACKSPACE and self.showScreen < 10 and self.showScreen > 2 and len(self.input[0]) > 0:
      self.input[0] = self.input[0][:-1]
    elif util.is_letter(key):
      charKey = str(chr(key))
      if charKey == " ":
        if self.showScreen < 2:
          self.showScreen += 1
        elif self.showScreen == 2:
          if self.bill["oxen"] > 0:
            print("Leaving store with: "+str(self.bill))
            print("Price: $"+str(util.calculate_bill(self.bill))+"0")
            self.next = SplashScreen(self.data, Landmarks.Landmarks.INDEPENDENCE, OptionsScreen(self.data))
          else:
            self.next = AlertScreen(self.data, "You need some oxen to\npull your wagon!")
      elif self.showScreen > 2 and self.showScreen < 10 and self.isNumber(charKey):
        self.input[0] += charKey
      elif self.showScreen == 2 and self.isNumber(charKey):
        self.showScreen = int(charKey) + 2

  def get_max(self, index):
    maxes = [9, 2000, 99, 99]
    return maxes[index]