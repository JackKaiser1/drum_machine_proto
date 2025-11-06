import pygame
from pygame import mixer 
import customtkinter
import time
from sound_class import Sample

# root = customtkinter.CTk()

# root.geometry("500x500")
# root.title("Sound Test")

# kick_button = customtkinter.CTkButton(root, text="KICK", height=80, width=80, command=play_kick)
# kick_button.grid(row=0, column=0)

# clap_button = customtkinter.CTkButton(root, text="CLAP", height=80, width=80, command=play_clap)
# clap_button.grid(row=0, column=1)

pygame.mixer.init(channels=1)
pygame.mixer.music.set_volume(0.8)

# kick = pygame.mixer.Sound("drum_kit/Kick Short.wav")
kick = Sample("drum_kit/Kick Short.wav")
snare = Sample("drum_kit/Snare Bright.wav")
clap = Sample("drum_kit/Clap.wav")
hihat = Sample("drum_kit/Hihat.wav")
rim = Sample("drum_kit/Rimshot.wav")
cowbell = Sample("drum_kit/Cowbell.wav")
cymbal = Sample("drum_kit/Cymbal.wav")
open_hat = Sample("drum_kit/Open Hat Short.wav")
maracas = Sample("drum_kit/Maracas.wav")
claves = Sample("drum_kit/Claves.wav")
tom_low = Sample("drum_kit/Tom Low.wav")
tom_mid = Sample("drum_kit/Tom Mid.wav")
tom_hi = Sample("drum_kit/Tom High.wav")
conga_low = Sample("drum_kit/Conga Low.wav")
conga_mid = Sample("drum_kit/Conga Mid.wav")
conga_hi = Sample("drum_kit/Conga High.wav")

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)


def play_clap():
    channel1.play(clap)

def play_kick():
    channel2.play(kick)

def play_rim():
    channel3.play(rim)

def play_snare():
    channel4.play(snare)

def play_hihat():
    channel5.play(hihat)
    
# kick_hits = []

def loop():
    # rim_hits = [7, 8, 16]
    # snare_hits = [5, 13] 
    # # kick_hits = [1, 9]
    # hihat_hits = range(1, 16)
    # clap_hits = [11]
    count = 0
    loop_count = 0
    while loop_count < 2:
        count += 1
        if count in kick.beat_list:
            play_kick()
        if count in snare.beat_list:
            play_snare()
        if count in rim.beat_list:
            play_rim()
        if count in hihat.beat_list:
            play_hihat()
        if count in clap.beat_list:
            play_clap()

        if count == 16:
            count = 0
            loop_count += 1
            

        time.sleep(0.2)



pause = False

def play():
    loop()

def pause():
    pause = True
    return pause
    # pygame.mixer.pause()



# loop()


# root.mainloop()