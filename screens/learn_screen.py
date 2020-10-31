from screens.screen import Screen
import pygame


class LearnScreen(Screen):
  def __init__(self):
    self.page = 0
    print("Learn screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 29)
    title = font.render('The Oregon Trail', True, WHITE)
    font = pygame.font.Font('font/font.ttf', 15)
    space = font.render('Press SPACE to continue.', True, WHITE)
    if self.page == 0:
      self.render_multiline("Try taking a journey by\ncovered wagon across 2000\nmiles of plains, rivers,\nand mountains. Try! On\nthe plains, will you sloth\nyour oxen through mud and\nwater-filled ruts or will\nyou plod through dust six\ninches deep?", 35, 120, screen)
    elif self.page == 1:
      self.render_multiline("How will you cross the\nrivers? If you have money,\nyou might take a ferry (if\nthere is a ferry). Or,\nyou can ford the river\nand hope you and your\nwagon aren't swallowed\nalive!\n\nWhat about supplies? Well,\nif you're low on food you\ncan hunt. You might get a\nbuffalo, you might. And\nthere are bears in\nthe mountains.", 35, 120, screen)
    elif self.page == 2:
      self.render_multiline("At the Dalles, you can try\nnavigating the Columbia\nRiver, but if running the\nrapids with a makeshift\nraft makes you queasy,\nbetter take the Barlow\nRoad.\n\nIf for some reason you\ndon't survive -- your\nwagon burns, or thieves\nsteal your oxen, or you\nrun out of provisions, or\nyou die of cholera --\ndon't give up! Try again\n...and again...and see how\nhigh your score can get.", 35, 120, screen)
    elif self.page == 3:
      self.render_multiline("Developed by:\n\nJack Richard\nSeamus Smith\nBenedict Antwi\nDamian Jadczak\nGabriel Palomeque Jara\nPrince Nanakobi", 35, 120, screen)
    screen.blit(title, (24, 40))
    screen.blit(space, (75, 475))

  def process_input(self, key):
    charKey = str(chr(key))
    if charKey == " ":
      if not self.page == 3:
        self.page = self.page + 1
      else:
        return None
    return self

  def render_multiline(self, text, x, y, screen):
    font = pygame.font.Font('font/font.ttf', 18)
    lines = text.splitlines()
    for i, l in enumerate(lines):
      screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + 19 * i))
