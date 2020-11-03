from screens.screen import Screen
import pygame


class NameSelectorScreen(Screen):
  def __init__(self):
    self.names = ["", "", "", "", ""]
    self.selected = 0
    print("Name selector screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    screen.fill(background)
    font = pygame.font.Font('font/font.ttf', 29)
    title = font.render('The Oregon Trail', True, WHITE)
    self.render_multiline_field('What is the first name of\nthe wagon leader? ', self.names[0], 25, 240, screen, self.selected == 0)
    if self.selected > 0:
      for i in range(4):
        font = pygame.font.Font('font/font.ttf', 17)
        self.render_multiline_field("#"+str(i+2)+": ",self.names[i+1], 25, 300+(i*30), screen, self.selected == i+1)
    screen.blit(title, (24, 40))

  def process_input(self, key):
    if key == pygame.K_RETURN:
      if self.selected < 4:
        self.selected += 1
      else:
        # TODO: something here
        print("done with names")
    elif key == pygame.K_BACKSPACE:
      if len(self.names[self.selected]) > 0:
        self.names[self.selected] = self.names[self.selected][:-1]
    elif len(self.names[self.selected]) < 12:
      # TODO: capital letter crash
      charKey = str(chr(key))
      self.names[self.selected] += charKey
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