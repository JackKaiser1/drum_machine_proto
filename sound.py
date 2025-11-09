import pygame
from pygame import mixer 
from sound_class import Sample, Count


pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(16)
pygame.mixer.music.set_volume(0.8)

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
channel6 = pygame.mixer.Channel(5)
channel7 = pygame.mixer.Channel(6)
channel8 = pygame.mixer.Channel(7)
channel9 = pygame.mixer.Channel(8)
channel10 = pygame.mixer.Channel(9)
channel11 = pygame.mixer.Channel(10)
channel12 = pygame.mixer.Channel(11)
channel13 = pygame.mixer.Channel(12)
channel14 = pygame.mixer.Channel(13)
channel15 = pygame.mixer.Channel(14)
channel16 = pygame.mixer.Channel(15)


def play_kick():
    channel2.play(kick)
def play_snare():
    channel4.play(snare)
def play_clap():
    channel1.play(clap)
def play_hihat():
    channel5.play(hihat)
def play_rim():
    channel3.play(rim)
def play_cowbell():
    channel6.play(cowbell)
def play_cymbal():
    channel7.play(cymbal)
def play_open_hat():
    channel8.play(open_hat)
def play_maracas():
    channel9.play(maracas)
def play_claves():
    channel10.play(claves)
def play_tom_low():
    channel11.play(tom_low)
def play_tom_mid():
    channel12.play(tom_mid)
def play_tom_hi():
    channel13.play(tom_hi)
def play_conga_low():
    channel14.play(conga_low)
def play_conga_mid():
    channel15.play(conga_mid)
def play_conga_hi():
    channel16.play(conga_hi)

count = Count()

def loop():
    count.count += 1
    if count.count in kick.beat_list:
        play_kick()
    if count.count in snare.beat_list:
        play_snare()
    if count.count in clap.beat_list:
        play_clap()
    if count.count in hihat.beat_list:
        play_hihat()
    if count.count in rim.beat_list:
        play_rim()
    if count.count in cowbell.beat_list:
        play_cowbell()
    if count.count in cymbal.beat_list:
        play_cymbal()
    if count.count in open_hat.beat_list:
        play_open_hat()
    if count.count in maracas.beat_list:
        play_maracas()
    if count.count in claves.beat_list:
        play_claves()
    if count.count in tom_low.beat_list:
        play_tom_low()
    if count.count in tom_mid.beat_list:
        play_tom_mid()
    if count.count in tom_hi.beat_list:
        play_tom_hi()
    if count.count in conga_low.beat_list:
        play_conga_low()
    if count.count in conga_mid.beat_list:
        play_conga_mid()
    if count.count in conga_hi.beat_list:
        play_conga_hi()


    if count.count == 16:
        count.count = 0

