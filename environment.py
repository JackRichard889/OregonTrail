from enum import Enum
import pygame

class Landmarks:
  class Landmarks(Enum):
    INDEPENDENCE = 0
    FORT_KEARNEY = 1
    CHIMNEY_ROCK = 2
    FORT_LARAMIE = 3
    INDEPENDENCE_ROCK = 4
    SOUTH_PASS = 5
    SODA_SPRINGS = 6
    FORT_BRIDGER = 7
    FORT_HALL = 8
    FORT_BOISE = 9
    BLUE_MOUNTAINS = 10
    FORT_WALLA_WALLA = 11
    THE_DALLES = 12
  names = {
    Landmarks.INDEPENDENCE: "Independence, Missouri",
    Landmarks.FORT_KEARNEY: "Fort Kearney",
    Landmarks.CHIMNEY_ROCK: "Chimney Rock",
    Landmarks.FORT_LARAMIE: "Fort Laramie",
    Landmarks.INDEPENDENCE_ROCK: "Independence Rock",
    Landmarks.SOUTH_PASS: "South Pass",
    Landmarks.SODA_SPRINGS: "Soda Springs",
    Landmarks.FORT_BRIDGER: "Fort Bridger",
    Landmarks.FORT_HALL: "Fort Hall",
    Landmarks.FORT_BOISE: "Fort Boise",
    Landmarks.BLUE_MOUNTAINS: "Blue Mountains",
    Landmarks.FORT_WALLA_WALLA: "Fort Walla Walla",
    Landmarks.THE_DALLES: "The Dalles"
  }
  assets = {
    Landmarks.INDEPENDENCE: pygame.image.load("screens/assets/landmarks/independence.jpg"),
    Landmarks.FORT_KEARNEY: pygame.image.load("screens/assets/landmarks/fort_kearney.png"),
    Landmarks.CHIMNEY_ROCK: pygame.image.load("screens/assets/landmarks/chimney_rock.png"),
    Landmarks.FORT_LARAMIE: pygame.image.load("screens/assets/landmarks/fort_laramie.png"),
    Landmarks.INDEPENDENCE_ROCK: pygame.image.load("screens/assets/landmarks/independence_rock.png"),
    Landmarks.SOUTH_PASS: pygame.image.load("screens/assets/landmarks/south_pass.png"),
    Landmarks.SODA_SPRINGS: pygame.image.load("screens/assets/landmarks/soda_springs.png"),
    Landmarks.FORT_BRIDGER: pygame.image.load("screens/assets/landmarks/fort_bridger.png"),
    Landmarks.FORT_HALL: pygame.image.load("screens/assets/landmarks/fort_hall.png"),
    Landmarks.FORT_BOISE: pygame.image.load("screens/assets/landmarks/fort_boise.png"),
    Landmarks.BLUE_MOUNTAINS: pygame.image.load("screens/assets/landmarks/blue_mountains.png"),
    Landmarks.FORT_WALLA_WALLA: pygame.image.load("screens/assets/landmarks/fort_walla_walla.png"),
    Landmarks.THE_DALLES: pygame.image.load("screens/assets/landmarks/the_dalles.png")
  }

class Environment:
    def __init__(self, name: str, texture, length: int):
        self.name = name
        self.texture = texture
        self.length = length


class EnvironmentRegistry:
    def __init__(self):
        self.__environments = []

    def add_environment(self, environment):
        self.__environments.append(environment)
        return len(self.__environments) - 1

    def get_environment(self, index):
        return self.__environments[index]

    def get_array(self):
        return self.__environments

    def get_length(self):
        length = 0
        for env in self.__environments:
            length += env.length * 100
        return length
