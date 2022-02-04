from turtle import getscreen
import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('othello')
running = True
while running:
    screen.fill((0,255,0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()