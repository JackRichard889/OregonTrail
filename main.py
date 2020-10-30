import pygame
from date import Date

WIDTH, HEIGHT = 500, 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oregon Trail 2020 Remastered Ultimate Edition")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

WHITE = (255, 255, 255)
background = (1, 1, 1)

screen.fill(background)

font = pygame.font.SysFont(None, 75)#Font and Size
img = font.render('The Oregon Trail', True, WHITE)#Text, N/A, Color
screen.blit(img, (20, 20))#what to display, position.

def main():
  running = True
  while running:
    for event in pygame.event.get():
      if event == pygame.QUIT:
        running = False
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
  main()

# testing from VSCode
# new one