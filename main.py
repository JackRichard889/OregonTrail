import pygame
from screens.main_screen import MainScreen

WIDTH, HEIGHT = 500, 500

currentScreen = MainScreen()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
background = (0, 0, 0)

screen.fill(background)

font = pygame.font.Font('font/font.ttf', 29)
img = font.render('The Oregon Trail', True, WHITE)
screen.blit(img, (24, 20))

def main():
  running = True
  while running:
    for event in pygame.event.get():
      if event == pygame.QUIT:
        running = False
      elif event == pygame.KEYDOWN:
        currentScreen.processInput(event.key)
    currentScreen.render(screen)
    pygame.display.update()
    clock.tick(60)

main()