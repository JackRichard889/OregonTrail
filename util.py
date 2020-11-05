import pygame

def imgscale(image, scale):
  return pygame.transform.scale(image, (image.get_size()[0] * scale, image.get_size()[1] * scale))