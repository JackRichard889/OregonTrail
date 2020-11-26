from enum import Enum
from random import choices

#####################
#    Person Class   #
#  By Jack Richard  #
#####################


class Disease:
    class Affects(Enum):
        PERSON = 0
        OXEN = 1

    affectsList = {Affects.PERSON: [], Affects.OXEN: []}

    def __init__(self, name, probability, affects, fatal):
        self.name = name
        self.probability = probability
        self.affects = affects
        self.fatal = fatal
        self.affectsList[affects].append(self)


class DiseaseList(Enum):
    CHOLERA = Disease("Cholera", 0.1, Disease.Affects.PERSON, True)
    DIPHTHERIA = Disease("Diphtheria", 0.1, Disease.Affects.PERSON, True)
    DYSENTERY = Disease("Dysentery", 0.2, Disease.Affects.PERSON, True)
    MEASLES = Disease("Measles", 0.1, Disease.Affects.PERSON, True)
    TYPHOID = Disease("Typhoid Fever", 0.1, Disease.Affects.PERSON, True)
    SNAKEBITE = Disease("Snakebite", 0.1, Disease.Affects.PERSON, True)
    DROWNING = Disease("Drowning", 0.0, Disease.Affects.PERSON, True)
    GUNSHOT = Disease("Gunshot Wound", 0.0, Disease.Affects.PERSON, True)
    EXHAUSTION = Disease("Exhaustion", 0.0, Disease.Affects.PERSON, True)
    BROKEN_ARM = Disease("Broken Arm", 0.0, Disease.Affects.PERSON, False)
    BROKEN_LEG = Disease("Broken Leg", 0.0, Disease.Affects.PERSON, False)
    HEALTHY = Disease("Healthy", 1, Disease.Affects.PERSON, False)
    INJURY = Disease("Injured", 0.1, Disease.Affects.OXEN, True)
    ROBBERY = Disease("Robbery", 0.1, Disease.Affects.OXEN, True)


class Person:
    def __init__(self, name, is_main_person, alive, occupation=-1):
        self.name = name
        self.health = 10
        self.is_main_person = is_main_person
        self.diseases = {}
        self.alive = alive
        self.occupation = occupation

    def update(self):
        for disease in self.diseases:
            self.diseases[disease] -= 1
            if self.diseases[disease] < 1:
                print("Should remove.")
                # TODO: remove element
        self.diseases[choices(
            Disease.affectsList[Disease.Affects.PERSON], [
                d.probability
                for d in Disease.affectsList[Disease.Affects.PERSON]
            ],
            k=1)[0]] = 3
        # TODO: add number of days to recovery
