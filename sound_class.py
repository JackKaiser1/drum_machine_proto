import pygame 
from pygame import mixer

class Sample(pygame.mixer.Sound):
    def __init__(self, filename):
        super().__init__(filename)
        self.beat_list = []
        self.filename = filename

class Drum():
    def __init__(self, drum_obj):
        self.drum_obj = drum_obj
