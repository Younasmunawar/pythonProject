import time,sys
import pygame
from pygame import mixer
pygame.mixer.init()
song=("test.wav")
pygame.mixer.music.load(song)
pygame.mixer.music.play()
time.sleep(40)