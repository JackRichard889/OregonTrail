import pygame
from math import *
from typing import Union
from person import Person
import random

# Image Scaling function
# By Seamus Smith
# Copyright 2020-HeatDeathOfTheUniverse
def imgscale(image: pygame.image , scale: Union[int, float]) -> pygame.image:
  return pygame.transform.scale(image,
  (round(image.get_size()[0] * scale), round(image.get_size()[1] * scale)))

# Image Scaling function in TWO DIMENSIONS
# By Seamus Smith
# Copyright 2020-UniverseBlackHoleDeath
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

# String Array to Person Array
# By Jack Richard
# Copyright 2020
def array_to_person(arrayNames, indexOfMain=0, arrayAlive=([True] * 5)):
  output = []
  for index in range(len(arrayNames)):
    output.append(Person(arrayNames[index], index == indexOfMain, arrayAlive[index]))
  return output

# Money For Profession Function
# By Jack Richard
# Copyright 2020
def money_for_profession(occupation):
  if occupation == 0:
    return 1600.00
  elif occupation == 1:
    return 800.00
  elif occupation == 2:
    return 400.00

# Random Name Generator
# By Jack Richard
# Copyright 2020
def random_name():
  names = ["Anna", "John", "Henry", "Jed", "Beth", "Zeke"]
  return random.choice(names)