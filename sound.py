import pygame
from pygame import mixer 
import customtkinter
import time

root = customtkinter.CTk()

root.geometry("500x500")
root.title("Sound Test")


pygame.mixer.init(channels=1)
# pygame.mixer.init()

# mixer.music.load("drum_kit/Clap.wav")
# mixer.music.load("drum_kit/Kick Basic.wav")
pygame.mixer.music.set_volume(0.8)
clap = pygame.mixer.Sound("drum_kit/Clap.wav")
kick = pygame.mixer.Sound("drum_kit/Kick Short.wav")
rim = pygame.mixer.Sound("drum_kit/Rimshot.wav")
snare = pygame.mixer.Sound("drum_kit/Snare Bright.wav")
hihat = pygame.mixer.Sound("drum_kit/Hihat.wav")

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)


def play_clap():
    # clap.set_volume(0.5)
    # clap.play(fade_ms=100)
    channel1.play(clap)

def play_kick():
    # kick.play()
    channel2.play(kick)

def play_rim():
    channel3.play(rim)

def play_snare():
    channel4.play(snare)

def play_hihat():
    channel5.play(hihat)
    

kick_button = customtkinter.CTkButton(root, text="KICK", height=80, width=80, command=play_kick)
kick_button.grid(row=0, column=0)

clap_button = customtkinter.CTkButton(root, text="CLAP", height=80, width=80, command=play_clap)
clap_button.grid(row=0, column=1)


def loop():
    rim_hits = [7, 8, 16]
    snare_hits = [5, 13] 
    kick_hits = [1, 9]
    hihat_hits = range(1, 16)
    clap_hits = [11]
    count = 0
    while True:
        count += 1
        if count in kick_hits:
            play_kick()
        if count in snare_hits:
            play_snare()
        if count in rim_hits:
            play_rim()
        if count in hihat_hits:
            play_hihat()
        if count in clap_hits:
            play_clap()

        if count == 16:
            count = 0

        time.sleep(0.2)



loop()


root.mainloop()