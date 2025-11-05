import customtkinter
from constants import *
import time
# from sound_map import sound_map
from sound import loop, play, pause, kick, snare, rim, hihat
import pygame
from pygame import mixer
from sound_class import sample, drum

root = customtkinter.CTk()

root.geometry("1205x800")
root.title("Drum Machine")


def pause_btn():
    for cell in cell_list:
        if int(cell._text) in drum_sound.drum_obj.beat_list:
            # if int(cell._text) == beat:
            print(int(cell._text))
            print(cell)
            cell.configure(fg_color="orange")
        elif cell._fg_color == "orange":
            cell.configure(fg_color="grey")

def record_button():
    play()


def click_cell(button, drum):
    beat = int(button._text)
  
                
            

    if button._fg_color == "grey": 
        drum.beat_list.append(beat)
        button.configure(fg_color="orange")
    else:
        drum.beat_list.remove(beat)
        button.configure(fg_color="grey")
    print(drum.beat_list)

drum_frame = customtkinter.CTkFrame(root)
button_frame = customtkinter.CTkFrame(root)
cell_frame = customtkinter.CTkFrame(root)
slider_frame = customtkinter.CTkFrame(root)

drum_frame.grid(row=6, column=1)
button_frame.grid(row=1, column=0, padx=5, pady=10)
cell_frame.grid(row=2, column=1, padx=0, pady=10)
slider_frame.grid(row=1, column=1, padx=5, pady=10) 

root.grid_rowconfigure(0, weight=0)

# drum_obj = None

drum_sound = drum(kick)


def drum_select(drum):
    if drum == "kick":
        drum_sound.drum_obj = kick
    elif drum == "snare":
        drum_sound.drum_obj = snare
    elif drum == "hihat":
        drum_sound.drum_obj = hihat
    elif drum == "rim":
        drum_sound.drum_obj = rim
    
    


   

    # print(drum_obj)
    # return drum_obj






kick_button = customtkinter.CTkButton(drum_frame, text="KICK", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command= lambda: drum_select("kick"))
snare_button = customtkinter.CTkButton(drum_frame, text="SNARE", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command= lambda: drum_select("snare"))
hihat_button = customtkinter.CTkButton(drum_frame, text="HIHAT", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command= lambda: drum_select("hihat"))
rim_button = customtkinter.CTkButton(drum_frame, text="RIM", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command= lambda: drum_select("rim"))


bpm_button = customtkinter.CTkButton(root, text="BPM", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
shift_button = customtkinter.CTkButton(button_frame, text="SHIFT", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
group_button = customtkinter.CTkButton(button_frame, text="GROUP", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
pattern_button = customtkinter.CTkButton(button_frame, text="PATTERN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command=pause_btn)
rec_button = customtkinter.CTkButton(root, text="REC", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command=record_button)
presets_button = customtkinter.CTkButton(root, text="Presets", height=50, width=200, fg_color="grey", hover_color="darkgrey")



cell_1 = customtkinter.CTkButton(cell_frame, text="1", height=55, width=55, command=lambda: click_cell(cell_1, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_2 = customtkinter.CTkButton(cell_frame, text="2", height=55, width=55, command=lambda: click_cell(cell_2, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_3 = customtkinter.CTkButton(cell_frame, text="3", height=55, width=55, command=lambda: click_cell(cell_3, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_4 = customtkinter.CTkButton(cell_frame, text="4", height=55, width=55, command=lambda: click_cell(cell_4, drum_sound.drum_obj), hover=None, fg_color="grey")

cell_5 = customtkinter.CTkButton(cell_frame, text="5", height=55, width=55, command=lambda: click_cell(cell_5, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_6 = customtkinter.CTkButton(cell_frame, text="6", height=55, width=55, command=lambda: click_cell(cell_6, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_7 = customtkinter.CTkButton(cell_frame, text="7", height=55, width=55, command=lambda: click_cell(cell_7, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_8 = customtkinter.CTkButton(cell_frame, text="8", height=55, width=55, command=lambda: click_cell(cell_8, drum_sound.drum_obj), hover=None, fg_color="grey")

cell_9 = customtkinter.CTkButton(cell_frame, text="9", height=55, width=55, command=lambda: click_cell(cell_9, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_10 = customtkinter.CTkButton(cell_frame, text="10", height=55, width=55, command=lambda: click_cell(cell_10, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_11 = customtkinter.CTkButton(cell_frame, text="11", height=55, width=55, command=lambda: click_cell(cell_11, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_12 = customtkinter.CTkButton(cell_frame, text="12", height=55, width=55, command=lambda: click_cell(cell_12, drum_sound.drum_obj), hover=None, fg_color="grey")

cell_13 = customtkinter.CTkButton(cell_frame, text="13", height=55, width=55, command=lambda: click_cell(cell_13, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_14 = customtkinter.CTkButton(cell_frame, text="14", height=55, width=55, command=lambda: click_cell(cell_14, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_15 = customtkinter.CTkButton(cell_frame, text="15", height=55, width=55, command=lambda: click_cell(cell_15, drum_sound.drum_obj), hover=None, fg_color="grey")
cell_16 = customtkinter.CTkButton(cell_frame, text="16", height=55, width=55, command=lambda: click_cell(cell_16, drum_sound.drum_obj), hover=None, fg_color="grey")

cell_list = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10, cell_11, cell_12, cell_13, cell_14, cell_15, cell_16]

slider_1 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_2 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_3 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_4 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_5 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_6 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_7 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_8 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_9 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_10 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_11 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_12 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_13 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_14 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_15 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_16 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")

slider_1.grid(row=4, column=1, padx=25)
slider_2.grid(row=4, column=2, padx=25)
slider_3.grid(row=4, column=3, padx=25)
slider_4.grid(row=4, column=4, padx=25)
slider_5.grid(row=4, column=5, padx=25)
slider_6.grid(row=4, column=6, padx=25)
slider_7.grid(row=4, column=7, padx=25)
slider_8.grid(row=4, column=8, padx=25)
slider_9.grid(row=4, column=9, padx=25)
slider_10.grid(row=4, column=10, padx=25)
slider_11.grid(row=4, column=11, padx=25)
slider_12.grid(row=4, column=12, padx=25)
slider_13.grid(row=4, column=13, padx=25)
slider_14.grid(row=4, column=14, padx=25)
slider_15.grid(row=4, column=15, padx=25)
slider_16.grid(row=4, column=16, padx=25)


bpm_button.grid(row=0, column=0, padx=20, pady=10)
shift_button.grid(row=1, column=0, padx=20, pady=10)
group_button.grid(row=2, column=0, padx=20, pady=10)
pattern_button.grid(row=3, column=0, padx=20, pady=10)
rec_button.grid(row=2, column=0, padx=10, pady=40)
presets_button.grid(row=0, column=1)

cell_1.grid(row=5, column=1, pady=5, padx=5.5)
cell_2.grid(row=5, column=2, pady=5, padx=5.5)
cell_3.grid(row=5, column=3, pady=5, padx=5.5)
cell_4.grid(row=5, column=4, pady=5, padx=5.5)
cell_5.grid(row=5, column=5, pady=5, padx=5.5)
cell_6.grid(row=5, column=6, pady=5, padx=5.5)
cell_7.grid(row=5, column=7, pady=5, padx=5.5)
cell_8.grid(row=5, column=8, pady=5, padx=5.5)
cell_9.grid(row=5, column=9, pady=5, padx=5.5)
cell_10.grid(row=5, column=10, pady=5, padx=5.5)
cell_11.grid(row=5, column=11, pady=5, padx=5.5)
cell_12.grid(row=5, column=12, pady=5, padx=5.5)
cell_13.grid(row=5, column=13, pady=5, padx=5.5)
cell_14.grid(row=5, column=14, pady=5, padx=5.5)
cell_15.grid(row=5, column=15, pady=5, padx=5.5)
cell_16.grid(row=5, column=16, pady=5, padx=5.5)

kick_button.grid(row=6, column=1, pady=10, padx=10)
snare_button.grid(row=6, column=2, pady=10, padx=10)
hihat_button.grid(row=6, column=3, pady=10, padx=10)
rim_button.grid(row=6, column=4, pady=10, padx=10)
        




root.mainloop()
