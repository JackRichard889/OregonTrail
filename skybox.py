import datetime as dt
import pygame
from typing import *

# Skybox Rendering Function
# By Seamus Smith
# Copyright 2020-(Infinity+1)

SKY_DAY = pygame.image.load("screens/assets/sky_day.png")
SKY_EVENING = pygame.image.load("screens/assets/sky_evening.png")
SKY_NIGHT = pygame.image.load("screens/assets/sky_night.png")

DUMMY_DATE = dt.datetime(1, 1, 1)
NOON = dt.time(12, 0, 0)
NOON_DELTA = dt.timedelta(minutes=720)

# All these functions can be added to util.py
def clamp(value, max_v, min_v) -> Union[int, float]:
    return max(min(value, max_v), min_v)

def get_percent_difference(original, new, bind = 100) -> float:
    return new / original * bind

# Get the difference between two time objects
def time_difference(first, second) -> dt.timedelta:
    datetime1 = dt.datetime.combine(DUMMY_DATE, first)
    datetime2 = dt.datetime.combine(DUMMY_DATE, second)
    return (datetime1 - datetime2)

# Gets the sum of two time objects
def add_time(first, second) -> dt.timedelta:
    datetime1 = dt.datetime.combine(DUMMY_DATE, first)
    datetime2 = dt.datetime.combine(DUMMY_DATE, second)
    return (datetime1 + datetime2)

# Draw to target screen with opacity
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

# Except this one. This one can be a method for the main game class (the one on the road) or it can be a function in the class' file
def render_skybox(screen, time: dt.time) -> None:
    day_progress = get_percent_difference(NOON_DELTA.total_seconds(), abs(time_difference(NOON, time).total_seconds()), 1)
    blit_alpha(screen, SKY_NIGHT, (0, 0), ((day_progress - 0.3) ** 3) * 255)
    blit_alpha(screen, SKY_EVENING, (0, 0), 255 - ((day_progress + 0.4) ** 2.2 * 255)) # i screwed around in desmos for so much time to get these equasions......
    blit_alpha(screen, SKY_DAY, (0, 0), 255 - ((day_progress + 0.5) ** 4 * 255))
