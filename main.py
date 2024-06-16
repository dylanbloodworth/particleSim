#! /usr/bin/python3

# Import pygame to visualize the particles
import pygame

# The pixel size for the square view window
screen_size = 500

class particle:
    def __init__(self, position, velocity : int = pygame.Vector2(0,0), radius : int = 10):
        self.radius = radius
        self.position = position 
        self.velocity = velocity 
        screen = pygame.display.get_surface()
        pygame.draw.circle(screen, "white", self.position, self.radius)
    

    def verBorderCheck(self):
        return (self.position.y > screen_size - 1.2*self.radius) or (self.position.y < 1.2*self.radius)

    def horBorderCheck(self):
        return (self.position.x > screen_size - 1.2*self.radius) or (self.position.x < 1.2*self.radius)


    def update(self, dt):
        self.velocity.y += 9.8*dt
        self.position.x = self.position.x + self.velocity.x*dt 
        self.position.y = self.position.y + self.velocity.y*dt 
    
        if self.verBorderCheck():
            self.velocity.y = -self.velocity.y
            print("hit floor")

        if self.horBorderCheck():
            self.velocity.x = -self.velocity.x
            print("hit left or right wall")



def main():
    
    pygame.init()
    screen = pygame.display.set_mode((screen_size, screen_size))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_vel = pygame.Vector2(0,-50)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False

        # fill the screen with a color to wipe away anything from last frame

        screen.fill("black")

        a = particle(player_pos, player_vel)

        a.update(dt)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
