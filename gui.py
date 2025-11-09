import customtkinter
from constants import *
import time
from sound_map import sample_map
from sound import loop, kick, snare, rim, hihat, count
import pygame
from pygame import mixer
from sound_class import Sample, Drum, Count
from button_frame import ButtonFrame
from cell_frame import CellFrame
from drum_select_frame import DrumSelectFrame
from slider_frame import SliderFrame




class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Init root window ------------------------------------------------
        self.title("Drum Machine")
        self.geometry("1220x650")
        self.grid_rowconfigure(0, weight=0)

        self.drum_sound = Drum(kick)
        self.is_paused = False
    

        # Init buttons ----------------------------------------------------
        self.bpm_button = customtkinter.CTkButton(self, text="BPM", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
        self.rec_button = customtkinter.CTkButton(self, text="REC", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command=self.record_button)
        self.presets_button = customtkinter.CTkButton(self, text="Presets", height=50, width=200, fg_color="grey", hover_color="darkgrey")

        # Position buttons ------------------------------------------------
        self.bpm_button.grid(row=0, column=0, padx=20, pady=10)
        self.rec_button.grid(row=3, column=0, padx=10, pady=10)
        self.presets_button.grid(row=0, column=1)


        # Init frames -----------------------------------------------------
        self.button_frame = ButtonFrame(self)
        self.cell_frame = CellFrame(self)
        self.slider_frame = SliderFrame(self)
        self.drum_select_frame = DrumSelectFrame(self)

        # Position frames
        self.button_frame.grid(row=1, column=0, padx=5, pady=10)
        self.cell_frame.grid(row=3, column=1, padx=0, pady=0)
        self.slider_frame.grid(row=1, column=1, padx=5, pady=10)
        self.drum_select_frame.grid(row=2, column=1, padx=0, pady=0)


    def record_button(self):
        if self.is_paused == True:
            self.is_paused = False
            self.cell_frame.display_beat().configure(fg_color=self.cell_frame.previous_color)
            self.cell_frame.i = -1
            return
        loop()
        self.cell_frame.display_beat()
        GUI.after(self, 110, self.record_button)
        


    def pause(self):
        if not self.is_paused:
            self.is_paused = True
            count.count = 0
        else:
            self.is_paused = False
        

gui = GUI()
gui.mainloop()

