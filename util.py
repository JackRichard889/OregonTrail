import pygame
from math import *
from typing import Union

# Image Scaling function
# By Seamus Smith
# Copyright 2020-HeatDeathOfTheUniverse
def imgscale(image: pygame.image , scale: Union[int, float]) -> pygame.image:
  return pygame.transform.scale(image,
  (round(image.get_size()[0] * scale), round(image.get_size()[1] * scale)))

def imgscale_2d(image: pygame.image , scaleX: Union[int, float], scaleY: Union[int, float]) -> pygame.image:
  return pygame.transform.scale(image,
  (round(image.get_size()[0] * scaleX), round(image.get_size()[1] * scaleY)))

# Is Letter Function
# By Jack Richard
# Copyright 2020
def is_letter(i: chr) -> bool:
  try: 
    chr(i)
    return True
  except ValueError:
    return False