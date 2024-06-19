import pygame

gravity: float = 9.8
position = pygame.Vector2(250, 400)
velocity = pygame.Vector2(0, 10)
particle_size = 10

positions = []
velocities = []

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('testing solving methods')
clock = pygame.time.Clock()


def update(dt):
    for i in range(0, len(positions)):
        velocities[i].y += gravity*dt
        positions[i].y += velocities[i].y*dt
        resolve_border_collisions(positions[i], velocities[i])
        pygame.draw.circle(screen, "purple", positions[i], particle_size)


def resolve_border_collisions(position, velocity):
    if (position.x > screen.get_width() - particle_size):
        position.x = screen.get_width() - particle_size
        velocity.x = - velocity.x

    if (position.x < particle_size):
        position.x = particle_size
        velocity.x = - velocity.x

    if (position.y > screen.get_height() - particle_size):
        position.y = screen.get_height() - particle_size
        velocity.y = - velocity.y

    if (position.y < particle_size):
        position.y = particle_size
        velocity.y = - velocity.y


def main():
    running = True

    while running:

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                positions.append(pygame.Vector2(mouse[0], mouse[1]))
                velocities.append(pygame.Vector2(0, 0))

        pygame.display.flip()
        screen.fill("black")

        dt = clock.tick(60)/100

        update(dt)


main()
