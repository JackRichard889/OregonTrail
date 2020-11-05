import pygame

def imgscale(image, scale):
  return pygame.transform.scale(image, (image.get_size()[0] * scale, image.get_size()[1] * scale))

def is_letter(self, i):
  try: 
    chr(i)
    return True
  except ValueError:
    return False