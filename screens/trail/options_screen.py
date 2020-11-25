from screens.screen import Screen
import pygame

class OptionsScreen(Screen):
  def __init__(self, data):
    self.data = data
    self.next = self
    self.idle = False
    self.input = [""]
    print("Options screen created.")

  def render(self, screen):
    WHITE = (255, 255, 255)
    background = (0, 0, 0)
    font = pygame.font.Font('font/font.ttf', 18)
    screen.fill(background)

    # Date
    date_text = font.render(self.data["date"].get_formatted_date(), True, WHITE)
    # Weather
    weather_text = font.render("Weather: "+self.data["date"].get_formatted_weather(self.data["date"].get_weather()), True, background)
    # Health
    health_text = font.render("Health: TODO", True, background)
    # Pace
    pace_formatted = ["steady", "strenuous", "grueling"]
    pace_text = font.render("Pace: "+pace_formatted[self.data["pace"]], True, background)
    # Rations
    rations_formatted = ["filling", "meager", "bare bones"]
    rations_text = font.render("Rations: "+rations_formatted[self.data["rations"]], True, background)

    # Options
    self.render_multiline("You may:\n\n  1. Continue on trail\n  2. Check supplies\n  3. Look at map\n  4. Change pace\n  5. Change food rations\n  6. Stop to rest\n  7. Attempt to trade\n  8. Hunt for food", 20, 200, screen)

    self.render_multiline_field("What is your choice? ", self.input[0], 20, 425, screen, True)

    screen.blit(date_text, date_text.get_rect(center=(500//2, 25)))
    pygame.draw.rect(screen, WHITE, pygame.Rect(30, 50, 440, 90))
    screen.blit(weather_text, weather_text.get_rect(center=(500//2, 64)))
    screen.blit(health_text, health_text.get_rect(center=(500//2, 84)))
    screen.blit(pace_text, pace_text.get_rect(center=(500//2, 104)))
    screen.blit(rations_text, rations_text.get_rect(center=(500//2, 124)))

  def process_input(self, key):
    # TODO: process input options
    print(key)