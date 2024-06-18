import pygame
from numpy_da import DynamicArray

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()



positions = []

running = True

while running:
    
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Added to Positions Array")
            add = pygame.Vector2(pos[0],pos[1])
            positions.append(add)
            print(positions)

    pygame.display.flip()

