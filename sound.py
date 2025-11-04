import pygame
from pygame import mixer 
import customtkinter

root = customtkinter.CTk()

root.geometry("500x500")
root.title("Sound Test")



mixer.init()

# mixer.music.load("drum_kit/Clap.wav")
# mixer.music.load("drum_kit/Kick Basic.wav")
mixer.music.set_volume(0.8)
clap = pygame.mixer.Sound("drum_kit/Clap.wav")
kick = pygame.mixer.Sound("drum_kit/Kick Basic.wav")

def play_clap():
    clap.play()

def play_kick():
    kick.play()

kick_button = customtkinter.CTkButton(root, text="KICK", height=80, width=80, command=play_kick)
kick_button.grid(row=0, column=0)

clap_button = customtkinter.CTkButton(root, text="CLAP", height=80, width=80, command=play_clap)
clap_button.grid(row=0, column=1)



root.mainloop()