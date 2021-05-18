import pygame
pygame.mixer.init()
pygame.mixer.music.load('../olhincima.mpeg')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass