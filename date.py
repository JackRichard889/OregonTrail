import datetime
from random import randint
from enum import Enum

#################################
#     Date Class v1.0           #
#     for Oregon Trail          #
#     by Jack Richard           #
#################################

class NoDateException(Exception):
  # throw when date is None
  pass

class Date:
  class Season(Enum):
    WINTER = 0
    SUMMER = 1
    SPRING = 2
    FALL = 3

  class Weather(Enum):
    NONE = 0
    SNOW = 1
    RAIN = 2
    FOG = 3
  
  def __init__(self, month, day):
    year = 1848
    month_temp = month
    if month_temp < 1:
      month_temp = randint(1, 12)
    day_temp = day
    if day_temp < 1:
      day_temp = randint(1, 25)
    self.date = datetime.datetime(year, month_temp, day_temp)

  def get_date(self):
    if self.date is None:
      raise NoDateException("FATAL! No date provided!")
    return self.date

  def get_formatted_date(self):
    months = {1: "January", 2: "February", 3: "March", 4: "April",
          5: "May", 6: "June", 7: "July", 8: "August",
          9: "September", 10: "October", 11: "November", 12: "December"}
    if self.date is None:
      raise NoDateException("FATAL! No date provided!")
      return None
    return months[self.date.month] + self.date.strftime(' %d, %Y')

  def get_season(self):
    season_for_month = {1: Date.Season.WINTER, 2: Date.Season.WINTER, 3: Date.Season.WINTER, 4: Date.Season.SPRING,
              5: Date.Season.SPRING, 6: Date.Season.SPRING, 7: Date.Season.SUMMER, 8: Date.Season.SUMMER,
              9: Date.Season.FALL, 10: Date.Season.FALL, 11: Date.Season.FALL, 12: Date.Season.WINTER}
    if self.date is None:
      raise NoDateException("FATAL! No date provided!")
      return None
    return season_for_month[self.date.month]

  def get_formatted_season(self, season):
    seasons = {Date.Season.WINTER: "Winter", Date.Season.FALL: "Fall",
           Date.Season.SPRING: "Spring", Date.Season.SUMMER: "Summer"}
    if self.date is None:
      raise NoDateException("FATAL! No date provided!")
      return None
    if season is None:
      raise NoDateException("FATAL! No date provided!")
      return None
    return seasons[season]

  def get_weather(self):
    weather = Date.Weather.NONE
    if self.get_season() == Date.Season.WINTER:
      weather = Date.Weather.SNOW
    elif self.get_season() == Date.Season.FALL:
      weather = Date.Weather.FOG
    elif self.get_season() == Date.Season.SPRING:
      weather = Date.Weather.RAIN

    if randint(0, 2) == 0:
      return weather
    else:
      return Date.Weather.NONE

  def get_formatted_weather(self, weather):
    weathers = {Date.Weather.NONE: "Clear", Date.Weather.RAIN: "Rain",
          Date.Weather.SNOW: "Snow", Date.Weather.FOG: "Fog"}
    if self.date is None:
      raise NoDateException("FATAL! No date provided!")
      return None
    if weather is None:
      raise Exception("FATAL! No weather provided!")
      return None
    return weathers[weather]

  def advance(self):
    return self.advance_days(1)

  def advance_days(self, days):
    if self.date is None:
      raise NoDateException("FATAL! No date provided!")
      return False
    self.date += datetime.timedelta(days=days)
    return True
