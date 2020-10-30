from screens.screen import Screen
import pygame


class MainScreen(Screen):
  def __init__(self):
    print("Main screen created.")
  def render(self, screen):
    print("Rendering")
  def processInput(self, key):
    print(key)