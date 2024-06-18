import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('testing solving methods')
clock = pygame.time.Clock()

dt = 0.05
current_pos = pygame.Vector2(255, 255)
velocity = pygame.Vector2(0,0)


last_pos = pygame.Vector2(255,255)

acceleration = 9.8


def update():
    velocity_y = current_pos.y - last_pos.y
    last_pos.y = current_pos.y
    current_pos.y += velocity_y + acceleration*dt*dt
    pygame.draw.circle(screen, "white", current_pos, 10)



def constraint():
    if current_pos.y > (screen.get_height()-10):
        velocity_y = current_pos.y - last_pos.y
        #print(f"Positions before changing: Current -> {current_pos.y} and Last {last_pos.y}")

        # This handles weirdness with the Verlet integration and the collisions at the boundaries. It's needed because we need the velocity to behave correctly when coming off the wall which means we need to set the last position past the bounding surface to correclty calculate the collisions.

        current_pos.y = screen.get_height() - 10
        last_pos.y = velocity_y + current_pos.y

        #print(f"Current Position {current_pos.y}")
        #print(f"Last Position {last_pos.y}")




def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        screen.fill("black")
        
        clock.tick(100)
        constraint()
        update()


main()

