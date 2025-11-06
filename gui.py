import customtkinter
from constants import *
import time
from sound_map import cell_map, sample_map
from sound import loop, play, pause, kick, snare, rim, hihat
import pygame
from pygame import mixer
from sound_class import Sample, Drum
# from seqencer_func import click_cell, drum_select, drum_sound





class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Init root window ------------------------------------------------
        self.title("Drum Machine")
        self.geometry("1220x650")
        self.grid_rowconfigure(0, weight=0)

        self.drum_sound = Drum(kick)
        self.select_mode = False

        def record_button():
            play()

        # Init buttons ----------------------------------------------------
        self.bpm_button = customtkinter.CTkButton(self, text="BPM", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
        self.rec_button = customtkinter.CTkButton(self, text="REC", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command=record_button)
        self.presets_button = customtkinter.CTkButton(self, text="Presets", height=50, width=200, fg_color="grey", hover_color="darkgrey")

        # Position buttons ------------------------------------------------
        self.bpm_button.grid(row=0, column=0, padx=20, pady=10)
        self.rec_button.grid(row=3, column=0, padx=10, pady=10)
        self.presets_button.grid(row=0, column=1)


        # Init frames -----------------------------------------------------
        self.button_frame = ButtonFrame(self)
        self.cell_frame = CellFrame(self)
        self.slider_frame = SliderFrame(self)
        self.drum_label_frame = DrumLabelFrame(self)

        # Position frames
        self.button_frame.grid(row=1, column=0, padx=5, pady=10)
        self.cell_frame.grid(row=3, column=1, padx=0, pady=0)
        self.slider_frame.grid(row=1, column=1, padx=5, pady=10)
        self.drum_label_frame.grid(row=2, column=1, padx=0, pady=0)


class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master):
            super().__init__(master)

            def select():
                master.select_mode = True
                print(master.select_mode)


            # Init buttons -------------------------------------------------
            self.select_button = customtkinter.CTkButton(self, text="SELECT", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command=select)
            self.group_button = customtkinter.CTkButton(self, text="GROUP", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
            self.pattern_button = customtkinter.CTkButton(self, text="PATTERN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")

            # Position buttons ----------------------------------------------
            self.select_button.grid(row=0, column=0, padx=20, pady=10)
            self.group_button.grid(row=1, column=0, padx=20, pady=10)
            self.pattern_button.grid(row=2, column=0, padx=20, pady=10)




class CellFrame(customtkinter.CTkFrame):
     def __init__(self, master):
        super().__init__(master)

        # Init cells -------------------------------------------------
        self.cell_1 = customtkinter.CTkButton(self, text="1", height=55, width=55, command=lambda: click_cell(self.cell_1, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_2 = customtkinter.CTkButton(self, text="2", height=55, width=55, command=lambda: click_cell(self.cell_2, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_3 = customtkinter.CTkButton(self, text="3", height=55, width=55, command=lambda: click_cell(self.cell_3, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_4 = customtkinter.CTkButton(self, text="4", height=55, width=55, command=lambda: click_cell(self.cell_4, master.drum_sound.drum_obj), hover=None, fg_color="grey")

        self.cell_5 = customtkinter.CTkButton(self, text="5", height=55, width=55, command=lambda: click_cell(self.cell_5, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_6 = customtkinter.CTkButton(self, text="6", height=55, width=55, command=lambda: click_cell(self.cell_6, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_7 = customtkinter.CTkButton(self, text="7", height=55, width=55, command=lambda: click_cell(self.cell_7, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_8 = customtkinter.CTkButton(self, text="8", height=55, width=55, command=lambda: click_cell(self.cell_8, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")

        self.cell_9 = customtkinter.CTkButton(self, text="9", height=55, width=55, command=lambda: click_cell(self.cell_9, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_10 = customtkinter.CTkButton(self, text="10", height=55, width=55, command=lambda: click_cell(self.cell_10, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_11 = customtkinter.CTkButton(self, text="11", height=55, width=55, command=lambda: click_cell(self.cell_11, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_12 = customtkinter.CTkButton(self, text="12", height=55, width=55, command=lambda: click_cell(self.cell_12, master.drum_sound.drum_obj), hover=None, fg_color="grey")

        self.cell_13 = customtkinter.CTkButton(self, text="13", height=55, width=55, command=lambda: click_cell(self.cell_13, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_14 = customtkinter.CTkButton(self, text="14", height=55, width=55, command=lambda: click_cell(self.cell_14, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_15 = customtkinter.CTkButton(self, text="15", height=55, width=55, command=lambda: click_cell(self.cell_15, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_16 = customtkinter.CTkButton(self, text="16", height=55, width=55, command=lambda: click_cell(self.cell_16, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")

        # Position cells ----------------------------------------------
        self.cell_1.grid(row=0, column=1, pady=5, padx=5.5)
        self.cell_2.grid(row=0, column=2, pady=5, padx=5.5)
        self.cell_3.grid(row=0, column=3, pady=5, padx=5.5)
        self.cell_4.grid(row=0, column=4, pady=5, padx=5.5)
        self.cell_5.grid(row=0, column=5, pady=5, padx=5.5)
        self.cell_6.grid(row=0, column=6, pady=5, padx=5.5)
        self.cell_7.grid(row=0, column=7, pady=5, padx=5.5)
        self.cell_8.grid(row=0, column=8, pady=5, padx=5.5)
        self.cell_9.grid(row=0, column=9, pady=5, padx=5.5)
        self.cell_10.grid(row=0, column=10, pady=5, padx=5.5)
        self.cell_11.grid(row=0, column=11, pady=5, padx=5.5)
        self.cell_12.grid(row=0, column=12, pady=5, padx=5.5)
        self.cell_13.grid(row=0, column=13, pady=5, padx=5.5)
        self.cell_14.grid(row=0, column=14, pady=5, padx=5.5)
        self.cell_15.grid(row=0, column=15, pady=5, padx=5.5)
        self.cell_16.grid(row=0, column=16, pady=5, padx=5.5)

        # Cell list --------------------------------------------------
        self.cell_list = [self.cell_1, self.cell_2, self.cell_3, self.cell_4, 
                          self.cell_5, self.cell_6, self.cell_7, self.cell_8, 
                          self.cell_9, self.cell_10, self.cell_11, self.cell_12, 
                          self.cell_13, self.cell_14, self.cell_15, self.cell_16]

        def click_cell(button, drum):
            beat = int(button._text)

            if master.select_mode:
                if beat in cell_map.keys():
                    drum_select(cell_map[beat])
                    master.select_mode = False
                    return

            if button._fg_color == "grey" or button._fg_color == "darkgrey": 
                drum.beat_list.append(beat)
                button.configure(fg_color="orange")
            elif beat in [5,6,7,8,13,14,15,16]:
                drum.beat_list.remove(beat)
                button.configure(fg_color="darkgrey")
            else:
                drum.beat_list.remove(beat)
                button.configure(fg_color="grey")
            print(drum.beat_list)


        def drum_select(drum):
            if drum in sample_map.keys():
                master.drum_sound.drum_obj = sample_map[drum]
            
            for cell in self.cell_list:
                cell_num = int(cell._text)
                beat_list = master.drum_sound.drum_obj.beat_list
                if cell_num in beat_list:
                    cell.configure(fg_color="orange")
                elif cell._fg_color == "orange":
                    if cell_num in [5,6,7,8,13,14,15,16]:
                        cell.configure(fg_color="darkgrey")
                    else:
                        cell.configure(fg_color="grey")



class SliderFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        # Init sliders -------------------------------------------------
        self.slider_1 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_2 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_3 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_4 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_5 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_6 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_7 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_8 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_9 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_10 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_11 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_12 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_13 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_14 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_15 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_16 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")


        # Position sliders ----------------------------------------------
        self.slider_1.grid(row=4, column=1, padx=25)
        self.slider_2.grid(row=4, column=2, padx=25)
        self.slider_3.grid(row=4, column=3, padx=25)
        self.slider_4.grid(row=4, column=4, padx=25)
        self.slider_5.grid(row=4, column=5, padx=25)
        self.slider_6.grid(row=4, column=6, padx=25)
        self.slider_7.grid(row=4, column=7, padx=25)
        self.slider_8.grid(row=4, column=8, padx=25)
        self.slider_9.grid(row=4, column=9, padx=25)
        self.slider_10.grid(row=4, column=10, padx=25)
        self.slider_11.grid(row=4, column=11, padx=25)
        self.slider_12.grid(row=4, column=12, padx=25)
        self.slider_13.grid(row=4, column=13, padx=25)
        self.slider_14.grid(row=4, column=14, padx=25)
        self.slider_15.grid(row=4, column=15, padx=25)
        self.slider_16.grid(row=4, column=16, padx=25)        


class DrumLabelFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Init Labels ------------------------------------------------------
        label1 = customtkinter.CTkLabel(self, text="KICK", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label2 = customtkinter.CTkLabel(self, text="SNARE", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label3 = customtkinter.CTkLabel(self, text="CLAP", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label4 = customtkinter.CTkLabel(self, text="HHAT", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label5 = customtkinter.CTkLabel(self, text="RIM", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label6 = customtkinter.CTkLabel(self, text="BELL", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label7 = customtkinter.CTkLabel(self, text="CRASH", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label8 = customtkinter.CTkLabel(self, text="OHAT", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label9 = customtkinter.CTkLabel(self, text="MARACAS", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label10 = customtkinter.CTkLabel(self, text="CLAV", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label11 = customtkinter.CTkLabel(self, text="TOM L", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label12 = customtkinter.CTkLabel(self, text="TOM M", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label13 = customtkinter.CTkLabel(self, text="TOM H", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label14 = customtkinter.CTkLabel(self, text="CONGA L", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label15 = customtkinter.CTkLabel(self, text="CONGA M", fg_color="grey", width=55, font=("Arial", 9), text_color="white")
        label16 = customtkinter.CTkLabel(self, text="CONGA H", fg_color="grey", width=55, font=("Arial", 9), text_color="white")

        # Position Labels -----------------------------------------------------
        label1.grid(row=0, column=0, padx=5.5, pady=5)
        label2.grid(row=0, column=1, padx=5.5, pady=5)
        label3.grid(row=0, column=2, padx=5.5, pady=5)
        label4.grid(row=0, column=3, padx=5.5, pady=5)
        label5.grid(row=0, column=4, padx=5.5, pady=5)
        label6.grid(row=0, column=5, padx=5.5, pady=5)
        label7.grid(row=0, column=6, padx=5.5, pady=5)
        label8.grid(row=0, column=7, padx=5.5, pady=5)
        label9.grid(row=0, column=8, padx=5.5, pady=5)
        label10.grid(row=0, column=9, padx=5.5, pady=5)
        label11.grid(row=0, column=10, padx=5.5, pady=5)
        label12.grid(row=0, column=11, padx=5.5, pady=5)
        label13.grid(row=0, column=12, padx=5.5, pady=5)
        label14.grid(row=0, column=13, padx=5.5, pady=5)
        label15.grid(row=0, column=14, padx=5.5, pady=5)
        label16.grid(row=0, column=15, padx=5.5, pady=5)


gui = GUI()
gui.mainloop()

