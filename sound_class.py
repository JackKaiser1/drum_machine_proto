import pygame 
from pygame import mixer

class sample(pygame.mixer.Sound):
    def __init__(self, filename):
        super().__init__(filename)
        self.beat_list = []
        self.filename = filename

class drum():
    def __init__(self, drum_obj):
        self.drum_obj = drum_obj
