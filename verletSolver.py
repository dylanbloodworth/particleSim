import pygame, numpy
from numpy_da import DynamicArray


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('testing solving methods')
clock = pygame.time.Clock()


gravity : float = 9.8;
position = pygame.Vector2(250,400)
velocity = pygame.Vector2(0, 100)
particle_size = 20


positions = DynamicArray(shape = 0, index_expansion = True)
velocities = DynamicArray(shape = 0, index_expansion = True)


def update(dt):
    velocity.y += gravity*dt
    position.y += velocity.y*dt

    resolve_border_collisions()
    pygame.draw.circle(screen, "red", position, particle_size)  

def resolve_border_collisions():
    if (position.y > screen.get_height()- particle_size):
        position.y = screen.get_height() - particle_size 
        velocity.y = - velocity.y
    
    if (position.y < particle_size):
        position.y = particle_size
        velocity.y = - velocity.y

def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        screen.fill("black")
    
        dt = clock.tick(1000)/250

        update(dt)


main()

