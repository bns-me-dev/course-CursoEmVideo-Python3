import pygame 

pygame.init()

print('21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.\n')
pygame.mixer.music.load('msc.mp3')
pygame.mixer.music.play()
pygame.event.wait()